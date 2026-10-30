# `AUHostExtensionContext`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSExtensionContext`
- 2 instance variables, 3 properties, 10 instance methods, 4 class methods

## Instance variables

```
@"NSExtension" _extension;
@"AUHostDelegate" _delegate;
```

## Properties

```
@property (T@"NSExtension",&,N,V_extension) extension;
@property (T@"AUHostDelegate",&,N,V_delegate) delegate;
@property (T@"NSXPCConnection",R,W,N) xpcConnection;
```

## Class methods

```
+[AUHostExtensionContext conformsToProtocol:];
+[AUHostExtensionContext _extensionAuxiliaryHostProtocol];
+[AUHostExtensionContext _extensionAuxiliaryVendorProtocol];
+[AUHostExtensionContext _allowedItemPayloadClasses];
```

## Instance methods

```
-[AUHostExtensionContext dealloc];
-[AUHostExtensionContext forwardingTargetForSelector:];
-[AUHostExtensionContext xpcConnection];
-[AUHostExtensionContext setDelegate:];
-[AUHostExtensionContext delegate];
-[AUHostExtensionContext conformsToProtocol:];
-[AUHostExtensionContext extension];
-[AUHostExtensionContext setExtension:];
-[AUHostExtensionContext initWithInputItems:listenerEndpoint:contextUUID:];
-[AUHostExtensionContext _derivedExtensionAuxiliaryHostProtocol];
```
