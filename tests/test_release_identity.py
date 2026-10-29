import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class ReleaseIdentityTests(unittest.TestCase):
    def read(self, relative_path):
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_new_app_distribution_identity(self):
        project = self.read("ios/project.yml")
        altstore = self.read("altstore/generate_source.py")
        workflow = self.read(".github/workflows/ios-build.yml")

        self.assertIn("PRODUCT_BUNDLE_IDENTIFIER: com.a16.bridgetts.gpt54mini", project)
        self.assertIn("PRODUCT_NAME: BridgeTTS54Mini", project)
        self.assertIn('MARKETING_VERSION: "2.10.0"', project)
        self.assertIn('"identifier": "com.a16.bridgetts.gpt54mini.source"', altstore)
        self.assertIn('"bundleIdentifier": "com.a16.bridgetts.gpt54mini"', altstore)
        self.assertIn("BridgeTTS-5.4-mini-unsigned.ipa", workflow)
        self.assertIn("name: BridgeTTS-5.4-mini-unsigned-ipa", workflow)
        self.assertIn("BridgeTTS54Mini.app", workflow)

    def test_original_distribution_identity_is_not_reused(self):
        distribution_files = [
            "ios/project.yml",
            "altstore/generate_source.py",
            ".github/workflows/ios-build.yml",
            "package.json",
            "app.js",
            "error-reporter.js",
        ]
        combined = "\n".join(self.read(path) for path in distribution_files)

        self.assertNotIn("com.a16.bridgetts.source", combined)
        self.assertNotIn("Bridge-TTS-Codex-", combined)
        self.assertNotIn("BridgeTTS-unsigned.ipa", combined)
        self.assertNotIn("BridgeTTS-unsigned-ipa", combined)

    def test_model_snapshot_and_parameters_are_fixed(self):
        translator = self.read("translator-service.js")
        evaluator = self.read("eval/run-eval.js")

        for content in (translator, evaluator):
            self.assertIn("gpt-5.6-luna", content)
            self.assertIn("reasoning_effort", content)
            self.assertIn("temperature: 0", content)
            self.assertIn("verbosity", content)


if __name__ == "__main__":
    unittest.main()
