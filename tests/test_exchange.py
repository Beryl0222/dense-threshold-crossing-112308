"""核对交换资料的字段和数值关系。"""
import json
from pathlib import Path
import unittest

import numpy as np


class ExchangeTests(unittest.TestCase):
    def setUp(self):
        source = Path(__file__).resolve().parents[1] / "data" / "exchange.json"
        self.data = json.loads(source.read_text(encoding="utf-8"))

    def test_exchange_data(self):
        steps=self.data['steps']
        s=steps[0]
        self.assertLess(sum(s['c']),self.data['threshold'])
        self.assertGreater(np.polynomial.polynomial.polyval(.5,s['c']),self.data['threshold'])
        self.assertAlmostEqual(np.polynomial.polynomial.polyval(.5,self.data['uncertain']['c']),self.data['threshold'])
