# `_TtC17AccessorySetupKit17ASUIClientManager`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
_$sSo18ASAccessorySessionCSgXw accessorySession;
_$sSaySo19ASPickerDisplayItemCG displayItems;
_$sSo6NSLockC activateLock;
DispatchQueue queue;
Swift.Error _$sSgcSg -> completionHandler;
(objc_protocol 0x247d77708) _$s_So19BSServiceConnectionCXcSg connection;
AccessorySetupKit.ASUIClientWrapper ? clientWrapper;
(objc_protocol 0x247d77710) ? server;
Swift.UInt64 startTicksFull;
_$sSi debounceCounter;
Swift.Bool pickerDidPresent;
Swift.Bool showPermissionPromptCalled;
```

## Class methods

```
+[_TtC17AccessorySetupKit17ASUIClientManager shared];
```

## Instance methods

```
-[_TtC17AccessorySetupKit17ASUIClientManager init];
-[_TtC17AccessorySetupKit17ASUIClientManager dealloc];
-[_TtC17AccessorySetupKit17ASUIClientManager activateConnectionWithSession:with:pickerSettings:for:requiresUI:completionHandler:];
-[_TtC17AccessorySetupKit17ASUIClientManager failWithAccessory:completionHandler:];
-[_TtC17AccessorySetupKit17ASUIClientManager finishDiscoveryWith:];
-[_TtC17AccessorySetupKit17ASUIClientManager showPermissionPromptWithServiceName:accessoryIdentifier:accessoryName:authorizationLevel:overrideBundleID:error:];
-[_TtC17AccessorySetupKit17ASUIClientManager showPermissionPromptWithServiceName:authorizationLevel:overrideBundleID:error:];
-[_TtC17AccessorySetupKit17ASUIClientManager updatePickerWith:completionHandler:];
-[_TtC17AccessorySetupKit17ASUIClientManager updateWithAccessory:options:for:completionHandler:];
```
