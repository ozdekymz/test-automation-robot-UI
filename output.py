<?xml version="1.0" encoding="UTF-8"?>
<robot generator="Robot 7.2.2 (Python 3.13.2 on win32)" generated="2025-02-20T15:26:24.002422" rpa="false" schemaversion="5">
<suite id="s1" name="InputBox" source="C:\Users\ozde\Desktop\VBIT Project\VBIT\robotframework-project\Training-2\InputBox.robot">
<test id="s1-t1" name="CheckingInputBox" line="6">
<kw name="Open Browser" owner="SeleniumLibrary">
<msg time="2025-02-20T15:26:24.449570" level="INFO">Opening browser 'chrome' to base url 'https://demo.nopcommerce.com/login?returnUrl=%2F'.</msg>
<arg>${URL}</arg>
<arg>${BROWSER}</arg>
<doc>Opens a new browser instance to the optional ``url``.</doc>
<status status="PASS" start="2025-02-20T15:26:24.448540" elapsed="4.985445"/>
</kw>
<kw name="Maximize Browser Window" owner="SeleniumLibrary">
<doc>Maximizes current browser window.</doc>
<status status="PASS" start="2025-02-20T15:26:29.434875" elapsed="0.049627"/>
</kw>
<kw name="Title Should Be" owner="SeleniumLibrary">
<msg time="2025-02-20T15:26:29.504431" level="INFO">Page title is 'nopCommerce demo store. Login'.</msg>
<arg>${title}</arg>
<doc>Verifies that the current page title equals ``title``.</doc>
<status status="PASS" start="2025-02-20T15:26:29.485346" elapsed="0.019841"/>
</kw>
<kw name="Set Variable" owner="BuiltIn">
<msg time="2025-02-20T15:26:29.507030" level="INFO">${"email_txt"} = id=Email</msg>
<var>${"email_txt"}</var>
<arg>id=Email</arg>
<doc>Returns the given values which can then be assigned to a variables.</doc>
<status status="PASS" start="2025-02-20T15:26:29.505931" elapsed="0.001592"/>
</kw>
<kw name="Element Should Be Visible" owner="SeleniumLibrary">
<msg time="2025-02-20T15:26:29.617222" level="INFO">Element 'id=Email' is displayed.</msg>
<arg>${"email_txt"}</arg>
<doc>Verifies that the element identified by ``locator`` is visible.</doc>
<status status="PASS" start="2025-02-20T15:26:29.508174" elapsed="0.109604"/>
</kw>
<kw name="Element Should Be Enabled" owner="SeleniumLibrary">
<arg>${"email_txt"}</arg>
<doc>Verifies that element identified by ``locator`` is enabled.</doc>
<status status="PASS" start="2025-02-20T15:26:29.618556" elapsed="0.038991"/>
</kw>
<kw name="Input Text" owner="SeleniumLibrary">
<msg time="2025-02-20T15:26:29.658832" level="INFO">Typing text 'johndoe@vodafone.com' into text field 'id=Email'.</msg>
<arg>${"email_txt"}</arg>
<arg>johndoe@vodafone.com</arg>
<doc>Types the given ``text`` into the text field identified by ``locator``.</doc>
<status status="PASS" start="2025-02-20T15:26:29.658083" elapsed="0.145619"/>
</kw>
<kw name="Sleep" owner="BuiltIn">
<msg time="2025-02-20T15:26:34.805527" level="INFO">Slept 5 seconds.</msg>
<arg>5</arg>
<doc>Pauses the test executed for the given time.</doc>
<status status="PASS" start="2025-02-20T15:26:29.804533" elapsed="5.001501"/>
</kw>
<kw name="Clear Element Text" owner="SeleniumLibrary">
<arg>${"email_txt"}</arg>
<doc>Clears the value of the text-input-element identified by ``locator``.</doc>
<status status="PASS" start="2025-02-20T15:26:34.806487" elapsed="0.081897"/>
</kw>
<kw name="Sleep" owner="BuiltIn">
<msg time="2025-02-20T15:26:37.889872" level="INFO">Slept 3 seconds.</msg>
<arg>3</arg>
<doc>Pauses the test executed for the given time.</doc>
<status status="PASS" start="2025-02-20T15:26:34.888985" elapsed="3.001444"/>
</kw>
<kw name="Close Browser" owner="SeleniumLibrary">
<doc>Closes the current browser.</doc>
<status status="PASS" start="2025-02-20T15:26:37.890847" elapsed="2.403623"/>
</kw>
<status status="PASS" start="2025-02-20T15:26:24.446512" elapsed="15.848521"/>
</test>
<status status="PASS" start="2025-02-20T15:26:24.016665" elapsed="16.279737"/>
</suite>
<statistics>
<total>
<stat pass="1" fail="0" skip="0">All Tests</stat>
</total>
<tag>
</tag>
<suite>
<stat name="InputBox" id="s1" pass="1" fail="0" skip="0">InputBox</stat>
</suite>
</statistics>
<errors>
</errors>
</robot>
