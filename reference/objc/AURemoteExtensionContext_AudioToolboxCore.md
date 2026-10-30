# `AURemoteExtensionContext`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSExtensionContext`
- 3 instance variables, 1 properties, 7 instance methods, 4 class methods

## Instance variables

```
@"AURemoteHost" _host;
B _isUIExtension;
@"AUAudioUnitViewService" _viewService;
```

## Properties

```
@property (T@"AUAudioUnitViewService",N,V_viewService) viewService;
```

## Class methods

```
+[AURemoteExtensionContext instancesRespondToSelector:];
+[AURemoteExtensionContext conformsToProtocol:];
+[AURemoteExtensionContext _extensionAuxiliaryHostProtocol];
+[AURemoteExtensionContext _extensionAuxiliaryVendorProtocol];
```

## Instance methods

```
-[AURemoteExtensionContext requestViewControllerWithCompletionHandler:];
-[AURemoteExtensionContext forwardingTargetForSelector:];
-[AURemoteExtensionContext initWithInputItems:listenerEndpoint:contextUUID:];
-[AURemoteExtensionContext setViewService:];
-[AURemoteExtensionContext iOSViewController];
-[AURemoteExtensionContext open:instanceUUID:reply:];
-[AURemoteExtensionContext viewService];
```
