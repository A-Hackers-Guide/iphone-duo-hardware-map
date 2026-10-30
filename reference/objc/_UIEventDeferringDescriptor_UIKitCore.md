# `_UIEventDeferringDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDebugDescriptionProviding`
- 12 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _compatibility;
I _predicateContextID;
i _targetPID;
I _targetContextID;
Q _scope;
@"BKSHIDEventDeferringEnvironment" _environment;
@"NSString" _displayHardwareIdentifier;
@"BKSHIDEventDeferringToken" _predicateLocalContainerToken;
@"NSString" _predicateSceneIdentityString;
^v _predicateWindowPointer;
@"NSString" _targetSceneIdentityString;
^v _targetWindowPointer;
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
-[_UIEventDeferringDescriptor debugDescription];
-[_UIEventDeferringDescriptor succinctDescriptionBuilder];
-[_UIEventDeferringDescriptor init];
-[_UIEventDeferringDescriptor descriptionWithMultilinePrefix:];
-[_UIEventDeferringDescriptor succinctDescription];
-[_UIEventDeferringDescriptor debugDescriptionWithMultilinePrefix:];
-[_UIEventDeferringDescriptor hash];
-[_UIEventDeferringDescriptor description];
-[_UIEventDeferringDescriptor copyWithZone:];
-[_UIEventDeferringDescriptor isEqual:];
-[_UIEventDeferringDescriptor descriptionBuilderWithMultilinePrefix:];
```
