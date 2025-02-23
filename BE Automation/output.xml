<?xml version="1.0" encoding="UTF-8"?>
<robot generator="Robot 5.0.1 (Python 3.10.12 on win32)" generated="20241114 15:07:36.273" rpa="false" schemaversion="3">
<suite id="s1" name="TC 1 GET Request" source="c:\Users\Ozde Naz Kaymaz\OneDrive - PIA-TEAM\Masaüstü\VBIT\robotframework-project\BE Automation\TC_1_GET_Request.robot">
<test id="s1-t1" name="Get_weatherInfo" line="9">
<kw name="Create Session" library="RequestsLibrary">
<arg>mysession</arg>
<arg>${base_url}</arg>
<doc>Create Session: create a HTTP session to a server</doc>
<msg timestamp="20241114 15:07:37.109" level="INFO">Creating Session using : alias=mysession, url=http://restapi.demoqa.com, headers={},                     cookies={}, auth=None, timeout=None, proxies=None, verify=False,                     debug=0 </msg>
<status status="PASS" starttime="20241114 15:07:37.101" endtime="20241114 15:07:37.120"/>
</kw>
<kw name="Get Request" library="RequestsLibrary">
<var>${response}</var>
<arg>mysession</arg>
<arg>/utilities/weather/city/${city} //response contains headers status code eg.</arg>
<doc>*DEPRECATED* Please use `GET On Session` instead.</doc>
<msg timestamp="20241114 15:07:37.120" level="WARN">Keyword 'RequestsLibrary.Get Request' is deprecated. Please use `GET On Session` instead.</msg>
<msg timestamp="20241114 15:07:37.354" level="WARN">Retrying (RetryAdapter(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NameResolutionError("&lt;urllib3.connection.HTTPConnection object at 0x0000027083B39480&gt;: Failed to resolve 'restapi.demoqa.com' ([Errno 11001] getaddrinfo failed)")': /utilities/weather/city/Delhi%20/response%20contains%20headers%20status%20code%20eg.</msg>
<msg timestamp="20241114 15:07:37.562" level="WARN">Retrying (RetryAdapter(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NameResolutionError("&lt;urllib3.connection.HTTPConnection object at 0x0000027083B39720&gt;: Failed to resolve 'restapi.demoqa.com' ([Errno 11001] getaddrinfo failed)")': /utilities/weather/city/Delhi%20/response%20contains%20headers%20status%20code%20eg.</msg>
<msg timestamp="20241114 15:07:37.966" level="WARN">Retrying (RetryAdapter(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NameResolutionError("&lt;urllib3.connection.HTTPConnection object at 0x0000027083B399C0&gt;: Failed to resolve 'restapi.demoqa.com' ([Errno 11001] getaddrinfo failed)")': /utilities/weather/city/Delhi%20/response%20contains%20headers%20status%20code%20eg.</msg>
<msg timestamp="20241114 15:07:37.974" level="FAIL">ConnectionError: HTTPConnectionPool(host='restapi.demoqa.com', port=80): Max retries exceeded with url: /utilities/weather/city/Delhi%20/response%20contains%20headers%20status%20code%20eg. (Caused by NameResolutionError("&lt;urllib3.connection.HTTPConnection object at 0x0000027083B39BA0&gt;: Failed to resolve 'restapi.demoqa.com' ([Errno 11001] getaddrinfo failed)"))</msg>
<status status="FAIL" starttime="20241114 15:07:37.120" endtime="20241114 15:07:38.023"/>
</kw>
<kw name="convert to string ${response.status_code} //we need to convert to this value to string format since the response returned as an integer value.">
<var>${status_code}</var>
<status status="NOT RUN" starttime="20241114 15:07:38.031" endtime="20241114 15:07:38.031"/>
</kw>
<kw name="Should Be Equal" library="BuiltIn">
<arg>${status_code}</arg>
<arg>200</arg>
<doc>Fails if the given objects are unequal.</doc>
<status status="NOT RUN" starttime="20241114 15:07:38.031" endtime="20241114 15:07:38.031"/>
</kw>
<kw name="Convert To String" library="BuiltIn">
<var>${body}</var>
<arg>${response.content} //we need to convert to this</arg>
<doc>Converts the given item to a Unicode string.</doc>
<status status="NOT RUN" starttime="20241114 15:07:38.031" endtime="20241114 15:07:38.031"/>
</kw>
<kw name="Should Contain" library="BuiltIn">
<arg>${body}</arg>
<arg>Delhi</arg>
<doc>Fails if ``container`` does not contain ``item`` one or more times.</doc>
<status status="NOT RUN" starttime="20241114 15:07:38.039" endtime="20241114 15:07:38.039"/>
</kw>
<kw name="Get From Dictionary" library="Collections">
<var>${contentTypeValue}</var>
<arg>${response.headers}</arg>
<arg>Content-Type</arg>
<doc>Returns a value from the given ``dictionary`` based on the given ``key``.</doc>
<status status="NOT RUN" starttime="20241114 15:07:38.039" endtime="20241114 15:07:38.039"/>
</kw>
<kw name="Should Be Equal" library="BuiltIn">
<arg>${contentTypeValue}</arg>
<arg>application/json</arg>
<doc>Fails if the given objects are unequal.</doc>
<status status="NOT RUN" starttime="20241114 15:07:38.039" endtime="20241114 15:07:38.039"/>
</kw>
<status status="FAIL" starttime="20241114 15:07:37.101" endtime="20241114 15:07:38.047">ConnectionError: HTTPConnectionPool(host='restapi.demoqa.com', port=80): Max retries exceeded with url: /utilities/weather/city/Delhi%20/response%20contains%20headers%20status%20code%20eg. (Caused by NameResolutionError("&lt;urllib3.connection.HTTPConnection object at 0x0000027083B39BA0&gt;: Failed to resolve 'restapi.demoqa.com' ([Errno 11001] getaddrinfo failed)"))</status>
</test>
<status status="FAIL" starttime="20241114 15:07:36.289" endtime="20241114 15:07:38.057"/>
</suite>
<statistics>
<total>
<stat pass="0" fail="1" skip="0">All Tests</stat>
</total>
<tag>
</tag>
<suite>
<stat pass="0" fail="1" skip="0" id="s1" name="TC 1 GET Request">TC 1 GET Request</stat>
</suite>
</statistics>
<errors>
<msg timestamp="20241114 15:07:37.120" level="WARN">Keyword 'RequestsLibrary.Get Request' is deprecated. Please use `GET On Session` instead.</msg>
<msg timestamp="20241114 15:07:37.354" level="WARN">Retrying (RetryAdapter(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NameResolutionError("&lt;urllib3.connection.HTTPConnection object at 0x0000027083B39480&gt;: Failed to resolve 'restapi.demoqa.com' ([Errno 11001] getaddrinfo failed)")': /utilities/weather/city/Delhi%20/response%20contains%20headers%20status%20code%20eg.</msg>
<msg timestamp="20241114 15:07:37.562" level="WARN">Retrying (RetryAdapter(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NameResolutionError("&lt;urllib3.connection.HTTPConnection object at 0x0000027083B39720&gt;: Failed to resolve 'restapi.demoqa.com' ([Errno 11001] getaddrinfo failed)")': /utilities/weather/city/Delhi%20/response%20contains%20headers%20status%20code%20eg.</msg>
<msg timestamp="20241114 15:07:37.966" level="WARN">Retrying (RetryAdapter(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NameResolutionError("&lt;urllib3.connection.HTTPConnection object at 0x0000027083B399C0&gt;: Failed to resolve 'restapi.demoqa.com' ([Errno 11001] getaddrinfo failed)")': /utilities/weather/city/Delhi%20/response%20contains%20headers%20status%20code%20eg.</msg>
</errors>
</robot>
