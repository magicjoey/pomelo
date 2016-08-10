#!/usr/bin/env python
# encoding: utf-8
"""
    @author: Magic Joey
    @contact: outlierw@gmail.com
    @site: http://underestimated.me
    @project: pomelo
    @description:
    @version: 2016-08-06 09:30,interceptor V1.0 
"""
class CommonDataProcessor(object):
    # Request预处理函数
    """
        这个方法的调用时机在 Django 接收到 request 之后，但仍未解析URL以确定应当运行的 view 之前。Django 向它传入相应的 HttpRequest 对象，以便在方法中修改。
        process_request() 应当返回 None 或 HttpResponse 对象。
        如果返回 None ，Django 将继续处理这个 request，执行后续的中间件， 然后调用相应的 view。
        如果返回 HttpResponse 对象，Django 将不再执行任何其它的中间件(无视其种类)以及相应的view。 Django将立即返回该 HttpResponse。
    """
    def process_request(self, request):
        # do nothing
        return None

    # View预处理函数:
    """
        这个方法的调用时机在 Django 执行完 request 预处理函数并确定待执行的 view 之后，但在 view 函数实际执行之前。
        request：HttpRequest 对象。
        callback：Django将调用的处理request的python函数. 这是实际的函数对象本身, 而不是字符串表述的函数名。
        args：将传入view的位置参数列表，但不包括 request 参数(它通常是传入view的第一个参数)。
        kwargs：将传入view的关键字参数字典。
        如同 process_request() , process_view() 应当返回 None 或 HttpResponse 对象。如果返回 None ， Django将继续处理这个 request ，执行后续的中间件， 然后调用相应的view。
        如果返回 HttpResponse 对象，Django 将不再执行 任何 其它的中间件(不论种类)以及相应的view，Django将立即返回。
    """
    def process_view(self, request, callback, callback_args, callback_kwargs):
        return None

    # Response后处理函数:
    """
        这个方法的调用时机在 Django 执行 view 函数并生成 response 之后。
        该处理器能修改 response 的内容；一个常见的用途是内容压缩，如 gzip 所请求的 HTML 页面。
        这个方法的参数相当直观： request 是 request 对象，而 response 则是从 view 中返回的 response 对象。
        process_response() 必须返回 HttpResponse 对象. 这个 response 对象可以是传入函数的那一个原始对象（通常已被修改），也可以是全新生成的。
    """
    def process_response(self, request, response):
        return response

    # Exception后处理函数:
    """
        这个方法只有在 request 处理过程中出了问题并且 view 函数抛出了一个未捕获的异常时才会被调用。这个钩子可以用来发送错误通知，将现场相关信息输出到日志文件，或者甚至尝试从错误中自动恢复。
        这个函数的参数除了一贯的 request 对象之外，还包括view函数抛出的实际的异常对象 exception 。
        process_exception() 应当返回 None 或 HttpResponse 对象。
        如果返回 None ， Django将用框架内置的异常处理机制继续处理相应request。
        如果返回 HttpResponse 对象，Django 将使用该response对象，而短路框架内置的异常处理机制。
    """
    def process_exception(self, request, exception):
        return None

