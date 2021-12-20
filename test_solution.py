# coding=utf-8
import pytest
import requests

# 1.請嘗試使用 Python 抓取 https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789, 
#   並利用 assert 確認 http response status code 為 200
# 2.請嘗試使用 Python 抓取 https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1, 
#   並利用 assert 確認 http response status code 為 403

class TestSuit:
    def test_URL1(self):
        resp = requests.get("https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789")
        assert resp.status_code == 200, "status_code is not 200 "
        
    def test_URL2(self):
        resp = requests.get("https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1")
        assert resp.status_code == 403, "status_code is not 403 "
