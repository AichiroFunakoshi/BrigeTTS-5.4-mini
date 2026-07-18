import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
REFERENCE_INSTRUCTION = (
    "上の文脈に代名詞・省略主語の参照先がある場合は、対象人物を訳文内で必ず明示し、"
    "代名詞だけまたは主語省略にしないこと。"
)


class MonotonicPromptTests(unittest.TestCase):
    def test_context_reference_instruction_is_shared_by_app_and_evaluator(self):
        for relative_path in ("app.js", "eval/run-eval.js"):
            source = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn(REFERENCE_INSTRUCTION, source, relative_path)


if __name__ == "__main__":
    unittest.main()
