# `_UIEventDeferringRecord`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`
- 5 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _recreationReasons;
@"_UIEventDeferringDescriptor" _descriptor;
@"<BSInvalidatable>" _invalidationToken;
@"_UIEventDeferringOwnershipToken" _deferringToken;
^v _recordingManagerPointer;
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
-[_UIEventDeferringRecord debugDescription];
-[_UIEventDeferringRecord succinctDescriptionBuilder];
-[_UIEventDeferringRecord init];
-[_UIEventDeferringRecord descriptionWithMultilinePrefix:];
-[_UIEventDeferringRecord succinctDescription];
-[_UIEventDeferringRecord debugDescriptionWithMultilinePrefix:];
-[_UIEventDeferringRecord description];
-[_UIEventDeferringRecord descriptionBuilderWithMultilinePrefix:];
```
