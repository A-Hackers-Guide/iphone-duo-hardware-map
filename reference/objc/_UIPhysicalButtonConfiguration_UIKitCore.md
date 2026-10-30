# `_UIPhysicalButtonConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `BSXPCSecureCoding`, `BSDebugDescriptionProviding`, `NSCopying`, `NSSecureCoding`
- 7 instance variables, 11 properties, 26 instance methods, 11 class methods

## Instance variables

```
B _wantsSystemShellExclusivePriority;
Q _button;
Q _behavior;
@"_UIPhysicalButtonBehaviorOptions" _behaviorOptions;
Q _generation;
@"BSAuditToken" _auditToken;
@"NSString" _name;
```

## Properties

```
@property (TQ,R,N,V_generation) _generation;
@property (TB,N,S_setWantsSystemShellExclusivePriority:,V_wantsSystemShellExclusivePriority) _wantsSystemShellExclusivePriority;
@property (TQ,R,N,V_button) _button;
@property (TQ,R,N,V_behavior) _behavior;
@property (T@"_UIPhysicalButtonBehaviorOptions",R,C,N) _behaviorOptions;
@property (T@"BSAuditToken",R,C,N,V_auditToken) _auditToken;
@property (T@"NSString",C,N,S_setName:,V_name) _name;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIPhysicalButtonConfiguration supportsBSXPCSecureCoding];
+[_UIPhysicalButtonConfiguration supportsSecureCoding];
+[_UIPhysicalButtonConfiguration _cameraCaptureShutterConfigurationWithOptionsProvider:];
+[_UIPhysicalButtonConfiguration _cameraShutterConfigurations];
+[_UIPhysicalButtonConfiguration _cameraShutterConfigurationsWithFilter:andOptionsProvider:];
+[_UIPhysicalButtonConfiguration _cameraShutterConfigurationsWithOptions:];
+[_UIPhysicalButtonConfiguration _cameraShutterConfigurationsWithOptionsProvider:];
+[_UIPhysicalButtonConfiguration _configurationWithPhysicalButton:behavior:behaviorOptions:];
+[_UIPhysicalButtonConfiguration _ringerButtonDynamicActionConfiguration];
+[_UIPhysicalButtonConfiguration _volumeCameraShutterConfigurationsWithOptionsProvider:];
+[_UIPhysicalButtonConfiguration _volumeConfigurations];
```

## Instance methods

```
-[_UIPhysicalButtonConfiguration _setName:];
-[_UIPhysicalButtonConfiguration _name];
-[_UIPhysicalButtonConfiguration debugDescription];
-[_UIPhysicalButtonConfiguration succinctDescriptionBuilder];
-[_UIPhysicalButtonConfiguration init];
-[_UIPhysicalButtonConfiguration initWithXPCDictionary:];
-[_UIPhysicalButtonConfiguration _button];
-[_UIPhysicalButtonConfiguration descriptionWithMultilinePrefix:];
-[_UIPhysicalButtonConfiguration _wantsSystemShellExclusivePriority];
-[_UIPhysicalButtonConfiguration _auditToken];
-[_UIPhysicalButtonConfiguration succinctDescription];
-[_UIPhysicalButtonConfiguration _generation];
-[_UIPhysicalButtonConfiguration debugDescriptionWithMultilinePrefix:];
-[_UIPhysicalButtonConfiguration encodeWithXPCDictionary:];
-[_UIPhysicalButtonConfiguration encodeWithCoder:];
-[_UIPhysicalButtonConfiguration _behaviorOptions];
-[_UIPhysicalButtonConfiguration hash];
-[_UIPhysicalButtonConfiguration description];
-[_UIPhysicalButtonConfiguration initWithCoder:];
-[_UIPhysicalButtonConfiguration encodeWithBSXPCCoder:];
-[_UIPhysicalButtonConfiguration initWithBSXPCCoder:];
-[_UIPhysicalButtonConfiguration _setWantsSystemShellExclusivePriority:];
-[_UIPhysicalButtonConfiguration copyWithZone:];
-[_UIPhysicalButtonConfiguration isEqual:];
-[_UIPhysicalButtonConfiguration _behavior];
-[_UIPhysicalButtonConfiguration descriptionBuilderWithMultilinePrefix:];
```
