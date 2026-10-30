# `_UIPhysicalButtonConfigurationSet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`, `NSCopying`, `NSMutableCopying`, `NSSecureCoding`, `BSXPCCoding`, `BSXPCSecureCoding`, `BSDebugDescriptionProviding`
- 2 instance variables, 5 properties, 23 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _configurationsByButton;
B _pauseButtonRequirementValidation;
```

## Properties

```
@property (TQ,R,N) _count;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIPhysicalButtonConfigurationSet supportsBSXPCSecureCoding];
+[_UIPhysicalButtonConfigurationSet supportsSecureCoding];
```

## Instance methods

```
-[_UIPhysicalButtonConfigurationSet _count];
-[_UIPhysicalButtonConfigurationSet mutableCopyWithZone:];
-[_UIPhysicalButtonConfigurationSet _configurationForButton:];
-[_UIPhysicalButtonConfigurationSet debugDescription];
-[_UIPhysicalButtonConfigurationSet succinctDescriptionBuilder];
-[_UIPhysicalButtonConfigurationSet init];
-[_UIPhysicalButtonConfigurationSet initWithXPCDictionary:];
-[_UIPhysicalButtonConfigurationSet _enumerateConfigurationsWithBlock:];
-[_UIPhysicalButtonConfigurationSet _configurationPassingTest:];
-[_UIPhysicalButtonConfigurationSet descriptionWithMultilinePrefix:];
-[_UIPhysicalButtonConfigurationSet succinctDescription];
-[_UIPhysicalButtonConfigurationSet debugDescriptionWithMultilinePrefix:];
-[_UIPhysicalButtonConfigurationSet encodeWithXPCDictionary:];
-[_UIPhysicalButtonConfigurationSet countByEnumeratingWithState:objects:count:];
-[_UIPhysicalButtonConfigurationSet encodeWithCoder:];
-[_UIPhysicalButtonConfigurationSet hash];
-[_UIPhysicalButtonConfigurationSet description];
-[_UIPhysicalButtonConfigurationSet initWithCoder:];
-[_UIPhysicalButtonConfigurationSet encodeWithBSXPCCoder:];
-[_UIPhysicalButtonConfigurationSet initWithBSXPCCoder:];
-[_UIPhysicalButtonConfigurationSet copyWithZone:];
-[_UIPhysicalButtonConfigurationSet isEqual:];
-[_UIPhysicalButtonConfigurationSet descriptionBuilderWithMultilinePrefix:];
```
