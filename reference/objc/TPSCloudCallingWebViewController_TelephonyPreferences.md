# `TPSCloudCallingWebViewController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIWebViewDelegate`
- 6 instance variables, 11 properties, 28 instance methods, 0 class methods

## Instance variables

```
q _type;
@"UIWebView" _webView;
@? _completionBlock;
@"UIActivityIndicatorView" _activityIndicator;
@"NSURL" _url;
@"NSData" _body;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"UIWebView",R,&,N,V_webView) webView;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@"UIActivityIndicatorView",&,N,V_activityIndicator) activityIndicator;
@property (T@"NSURL",&,N,V_url) url;
@property (T@"NSData",&,N,V_body) body;
@property (TB,R,N,GisPresentingURL) presentingURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSCloudCallingWebViewController webView];
-[TPSCloudCallingWebViewController body];
-[TPSCloudCallingWebViewController setCompletionBlock:];
-[TPSCloudCallingWebViewController completionBlock];
-[TPSCloudCallingWebViewController setBody:];
-[TPSCloudCallingWebViewController init];
-[TPSCloudCallingWebViewController initWithType:];
-[TPSCloudCallingWebViewController activityIndicator];
-[TPSCloudCallingWebViewController initWithNibName:bundle:];
-[TPSCloudCallingWebViewController setType:];
-[TPSCloudCallingWebViewController type];
-[TPSCloudCallingWebViewController loadView];
-[TPSCloudCallingWebViewController initWithCoder:];
-[TPSCloudCallingWebViewController setUrl:];
-[TPSCloudCallingWebViewController url];
-[TPSCloudCallingWebViewController setActivityIndicator:];
-[TPSCloudCallingWebViewController uiWebView:didClearWindowObject:forFrame:];
-[TPSCloudCallingWebViewController webView:didFailLoadWithError:];
-[TPSCloudCallingWebViewController _cancelButtonClicked:];
-[TPSCloudCallingWebViewController isPresentingURL];
-[TPSCloudCallingWebViewController cancelWebView];
-[TPSCloudCallingWebViewController doProvisioningCanceled];
-[TPSCloudCallingWebViewController doProvisioningDone];
-[TPSCloudCallingWebViewController doProvisioningFailed];
-[TPSCloudCallingWebViewController doWebViewTimedOut];
-[TPSCloudCallingWebViewController loadURL:body:completion:];
-[TPSCloudCallingWebViewController loadWebViewWithSpinner:];
-[TPSCloudCallingWebViewController setupControllerInWebFrame:];
```
