# `WFWebSheetViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `WFRemoteWebSheetViewControllerDelegate`, `WFNetworkView`
- 3 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"_UIAsyncInvocation" _cancelServiceInvocation;
@"WFRemoteWebSheetViewController" _remoteViewController;
@"<WFWebSheetViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"_UIAsyncInvocation",&,N,V_cancelServiceInvocation) cancelServiceInvocation;
@property (T@"WFRemoteWebSheetViewController",&,N,V_remoteViewController) remoteViewController;
@property (T@"<WFWebSheetViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,?,R,N) wantsModalPresentation;
```

## Instance methods

```
-[WFWebSheetViewController initWithDelegate:];
-[WFWebSheetViewController dealloc];
-[WFWebSheetViewController remoteViewController];
-[WFWebSheetViewController setDelegate:];
-[WFWebSheetViewController delegate];
-[WFWebSheetViewController setRemoteViewController:];
-[WFWebSheetViewController wantsModalPresentation];
-[WFWebSheetViewController _finishSetupWithError:];
-[WFWebSheetViewController _requestRemoteViewController];
-[WFWebSheetViewController cancelServiceInvocation];
-[WFWebSheetViewController setCancelServiceInvocation:];
-[WFWebSheetViewController _showRemoteViewController];
-[WFWebSheetViewController remoteWebSheetViewController:handleEvent:context:];
-[WFWebSheetViewController webSheetViewControllerServiceShouldTerminate];
```
