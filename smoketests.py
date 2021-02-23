from unittest import TestLoader, TestSuite, main as Main
from assertions import AssertionsTest
from searchtests import SearchTests
from HtmlTestRunner import HTMLTestRunner


class SuitTest(TestSuite):
    assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)  # carga una prueba a realizar
    search_tests = TestLoader().loadTestsFromTestCase(SearchTests)  # carga la otra prueba
    
    smoke_test = TestSuite([assertions_test, search_tests]) #Lista para pasar el reporte

# generar repote unificado
Main(testRunner=HTMLTestRunner(output='smoke-report',
                               report_name="Reporte",
                               combine_reports=True))