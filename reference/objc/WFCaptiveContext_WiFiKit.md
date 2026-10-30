# `WFCaptiveContext`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFWebSheetViewControllerDelegate`, `WFProviderContext`
- 7 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _readyForPresentation;
@"<WFNetworkListRecord>" network;
q requestedFields;
@? _readyForPresentationHandler;
@? _completionHandler;
@"WFWebSheetViewController" _webSheetViewController;
@"NSTimer" _timer;
```

## Properties

```
@property (T@"WFWebSheetViewController",&,N,V_webSheetViewController) webSheetViewController;
@property (T@"NSTimer",&,N,V_timer) timer;
@property (TB,N,V_readyForPresentation) readyForPresentation;
@property (T@?,C,N,V_readyForPresentationHandler) readyForPresentationHandler;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<WFNetworkListRecord>",R,N,Vnetwork) network;
@property (Tq,R,N,VrequestedFields) requestedFields;
```

## Instance methods

```
-[WFCaptiveContext setCompletionHandler:];
-[WFCaptiveContext setTimer:];
-[WFCaptiveContext completionHandler];
-[WFCaptiveContext network];
-[WFCaptiveContext init];
-[WFCaptiveContext timer];
-[WFCaptiveContext requestedFields];
-[WFCaptiveContext setReadyForPresentation:];
-[WFCaptiveContext cancel];
-[WFCaptiveContext setWebSheetViewController:];
-[WFCaptiveContext webSheetViewController];
-[WFCaptiveContext setReadyForPresentationHandler:];
-[WFCaptiveContext _presentationTimerFired:];
-[WFCaptiveContext _readyForPresentation:];
-[WFCaptiveContext readyForPresentation];
-[WFCaptiveContext readyForPresentationHandler];
-[WFCaptiveContext webSheetViewController:didTerminateWithError:];
-[WFCaptiveContext webSheetViewControllerContentReadyForPresentation:];
```
