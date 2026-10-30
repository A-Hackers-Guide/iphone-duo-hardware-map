# `WFPickerViewProvider`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFNetworkView`, `WFNetworkViewProvider`
- 3 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
B wantsModalPresentation;
@"<WFPickerViewProviderDelegate>" _delegate;
@"UIViewController" _rootViewController;
```

## Properties

```
@property (T@"UIViewController",&,N,V_rootViewController) rootViewController;
@property (T@"<WFPickerViewProviderDelegate>",W,N,V_delegate) delegate;
@property (TB,?,R,N,VwantsModalPresentation) wantsModalPresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFPickerViewProvider rootViewController];
-[WFPickerViewProvider setRootViewController:];
-[WFPickerViewProvider credentialsViewControllerWithContext:];
-[WFPickerViewProvider networkErrorViewControllerWithContext:];
-[WFPickerViewProvider setDelegate:];
-[WFPickerViewProvider certificateViewControllerWithContext:];
-[WFPickerViewProvider delegate];
-[WFPickerViewProvider presentNetworkViewController:forContext:];
-[WFPickerViewProvider networkDetailsViewControllerWithContext:];
-[WFPickerViewProvider initWithRootViewController:];
-[WFPickerViewProvider wantsModalPresentation];
-[WFPickerViewProvider didDismissNetworkViewController:forContext:];
-[WFPickerViewProvider otherNetworkViewControllerWithContext:];
-[WFPickerViewProvider _canHandleCredentialsContext:];
-[WFPickerViewProvider _promptForEnterpriseJoin:];
```
