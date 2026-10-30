# `UIWebViewWebViewDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WebFrameLoadDelegate`, `WebPolicyDelegate`, `WebResourceLoadDelegate`, `WebUIDelegate`
- 1 instance variables, 4 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"UIWebView" uiWebView;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWebViewWebViewDelegate _clearUIWebView];
-[UIWebViewWebViewDelegate webView:decidePolicyForMIMEType:request:frame:decisionListener:];
-[UIWebViewWebViewDelegate initWithUIWebView:];
-[UIWebViewWebViewDelegate webThreadWebView:resource:willSendRequest:redirectResponse:fromDataSource:];
-[UIWebViewWebViewDelegate webView:connectionPropertiesForResource:dataSource:];
-[UIWebViewWebViewDelegate webView:createWebViewWithRequest:];
-[UIWebViewWebViewDelegate webView:decidePolicyForGeolocationRequestFromOrigin:frame:listener:];
-[UIWebViewWebViewDelegate webView:decidePolicyForNavigationAction:request:frame:decisionListener:];
-[UIWebViewWebViewDelegate webView:decidePolicyForNewWindowAction:request:newFrameName:decisionListener:];
-[UIWebViewWebViewDelegate webView:didChangeLocationWithinPageForFrame:];
-[UIWebViewWebViewDelegate webView:didClearWindowObject:forFrame:];
-[UIWebViewWebViewDelegate webView:didCommitLoadForFrame:];
-[UIWebViewWebViewDelegate webView:didFailLoadWithError:forFrame:];
-[UIWebViewWebViewDelegate webView:didFailProvisionalLoadWithError:forFrame:];
-[UIWebViewWebViewDelegate webView:didFinishLoadForFrame:];
-[UIWebViewWebViewDelegate webView:didFirstLayoutInFrame:];
-[UIWebViewWebViewDelegate webView:didReceiveServerRedirectForProvisionalLoadForFrame:];
-[UIWebViewWebViewDelegate webView:didReceiveTitle:forFrame:];
-[UIWebViewWebViewDelegate webView:didStartProvisionalLoadForFrame:];
-[UIWebViewWebViewDelegate webView:exceededApplicationCacheOriginQuotaForSecurityOrigin:totalSpaceNeeded:];
-[UIWebViewWebViewDelegate webView:frame:exceededDatabaseQuotaForSecurityOrigin:database:];
-[UIWebViewWebViewDelegate webView:identifierForInitialRequest:fromDataSource:];
-[UIWebViewWebViewDelegate webView:printFrameView:];
-[UIWebViewWebViewDelegate webView:resource:canAuthenticateAgainstProtectionSpace:forDataSource:];
-[UIWebViewWebViewDelegate webView:resource:didCancelAuthenticationChallenge:fromDataSource:];
-[UIWebViewWebViewDelegate webView:resource:didFailLoadingWithError:fromDataSource:];
-[UIWebViewWebViewDelegate webView:resource:didFinishLoadingFromDataSource:];
-[UIWebViewWebViewDelegate webView:resource:didReceiveAuthenticationChallenge:fromDataSource:];
-[UIWebViewWebViewDelegate webView:runJavaScriptAlertPanelWithMessage:initiatedByFrame:];
-[UIWebViewWebViewDelegate webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame:];
-[UIWebViewWebViewDelegate webView:runJavaScriptTextInputPanelWithPrompt:defaultText:initiatedByFrame:];
-[UIWebViewWebViewDelegate webView:unableToImplementPolicyWithError:frame:];
-[UIWebViewWebViewDelegate webViewClose:];
-[UIWebViewWebViewDelegate webViewSupportedOrientationsUpdated:];
```
