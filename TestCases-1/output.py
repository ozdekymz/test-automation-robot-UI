<?xml version="1.0" encoding="UTF-8"?>
<robot generator="Robot 7.1 (Python 3.12.0 on win32)" generated="2024-10-11T11:36:11.712525" rpa="false" schemaversion="5">
<suite id="s1" name="TC1" source="C:\Users\Ozde Naz Kaymaz\Desktop\VBIT\robotframework-project\TestCases\TC1.robot">
<test id="s1-t1" name="LoginTest" line="7">
<kw name="Open Browser" owner="SeleniumLibrary">
<msg time="2024-10-11T11:36:11.973289" level="INFO">Opening browser 'chrome' to base url 'https://the-internet.herokuapp.com/login'.</msg>
<arg>${URL}</arg>
<arg>${BROWSER}</arg>
<doc>Opens a new browser instance to the optional ``url``.</doc>
<status status="PASS" start="2024-10-11T11:36:11.973289" elapsed="152.237995"/>
</kw>
<kw name="Maximize Browser Window" owner="SeleniumLibrary">
<doc>Maximizes current browser window.</doc>
<status status="PASS" start="2024-10-11T11:38:44.211284" elapsed="0.123294"/>
</kw>
<kw name="LoginToApp" owner="TC1_Keywords">
<kw name="Input Text" owner="SeleniumLibrary">
<msg time="2024-10-11T11:38:44.341681" level="INFO">Typing text 'tomsmith' into text field 'id=username'.</msg>
<arg>id=username</arg>
<arg>${USERNAME}</arg>
<doc>Types the given ``text`` into the text field identified by ``locator``.</doc>
<status status="PASS" start="2024-10-11T11:38:44.341681" elapsed="0.329802"/>
</kw>
<kw name="Input Password" owner="SeleniumLibrary">
<msg time="2024-10-11T11:38:44.671483" level="INFO">Typing password into text field 'id=password'.</msg>
<msg time="2024-10-11T11:38:44.781447" level="INFO">Temporally setting log level to: NONE</msg>
<arg>id=password</arg>
<arg>${PASSWORD}</arg>
<doc>Types the given password into the text field identified by ``locator``.</doc>
<status status="PASS" start="2024-10-11T11:38:44.671483" elapsed="0.279995"/>
</kw>
<kw name="Click Button" owner="SeleniumLibrary">
<msg time="2024-10-11T11:38:44.951478" level="INFO">Clicking button 'xpath=//button[@type='submit']'.</msg>
<arg>xpath=//button[@type='submit']</arg>
<doc>Clicks the button identified by ``locator``.</doc>
<status status="PASS" start="2024-10-11T11:38:44.951478" elapsed="48.500149"/>
</kw>
<status status="PASS" start="2024-10-11T11:38:44.341681" elapsed="49.109946"/>
</kw>
<kw name="Close Browser" owner="SeleniumLibrary">
<doc>Closes the current browser.</doc>
<status status="PASS" start="2024-10-11T11:39:33.451627" elapsed="2.406081"/>
</kw>
<status status="PASS" start="2024-10-11T11:36:11.973289" elapsed="203.884419"/>
</test>
<status status="PASS" start="2024-10-11T11:36:11.712525" elapsed="204.145183"/>
</suite>
<statistics>
<total>
<stat pass="1" fail="0" skip="0">All Tests</stat>
</total>
<tag>
</tag>
<suite>
<stat pass="1" fail="0" skip="0" id="s1" name="TC1">TC1</stat>
</suite>
</statistics>
<errors>
</errors>
</robot>
