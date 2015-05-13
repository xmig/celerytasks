"""
Provides Task Result Chaining
Copy tretiak@gmail.com / https://github.com/xmig
Any restriction for using
"""

import traceback
import logging as _logger


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
class ProxyValueMixin(object):
    ResultStatus = "result_status"

    def proxy(self, input_value, result_value, result_name=None):
        """ Mixin which help 'to proxy' values in case Tasks Chain
        :param input_value: <dict | none> Previous Task Result
        :param result_value: <any> Result
        :param result_name:  <str> Result Value Key
        :return:
        """
        if isinstance(input_value, dict):
            if isinstance(result_value, dict):
                for k, v in result_value.items():
                    input_value[k] = v
            else:
                if not result_name:
                    _logger.warn("Proxy value '{}' name is None")
                input_value[result_name] = result_value

                return input_value
        return result_value

    def get_proxy_value(self, proxy_value, result_name, default_value=None):
        proxy_value = proxy_value or {}
        if not isinstance(proxy_value, dict):
            _logger.warn("Cannot get key '{}' Because ProxyValue is not an DICT. "
                         "Entered value: [{}] Type: '{}'".format(result_name, proxy_value, type(proxy_value)))
            return default_value
        return proxy_value.get(result_name, default_value)

    def set_proxy_value(self, proxy_value, result_value, result_name=None):
        if proxy_value is None:
            proxy_value = {}
        self.proxy(proxy_value, result_value, result_name)
        return proxy_value

    def set_error(self, proxy_value):
        self.set_proxy_value(proxy_value, "ERROR", self.ResultStatus)
        return proxy_value

    def is_error(self, proxy_value):
        return self.get_proxy_value(proxy_value, self.ResultStatus) == "ERROR"

    def set_internal_error(self, proxy_value, mess=None, ex=None):
        self.set_proxy_value(proxy_value, "ERROR", self.ResultStatus)
        err_info = {"cls": type(self).__name__}
        if mess:
            err_info["mess"] = mess
        if ex:
            err_info["trace"] = traceback.format_exc()
            _logger.warn(err_info["trace"])

        proxy_value["error_info"] = err_info
        return proxy_value
