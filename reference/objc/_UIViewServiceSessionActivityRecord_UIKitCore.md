# `_UIViewServiceSessionActivityRecord`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`
- 10 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _associatedHostedWindows;
B _hasInvalidated;
i _lastViewControllerAppearState;
@"_UIActiveViewServiceSessionTracker" _tracker;
@"<_UIViewServiceSessionActivityProviding>" _lastActivityProvider;
Q _lastActivity;
Q _lastActivityTimestamp;
@"NSUUID" _sessionIdentifier;
q _userInterfaceIdiom;
@"UIWindow" _primaryHostedWindow;
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
-[_UIViewServiceSessionActivityRecord debugDescription];
-[_UIViewServiceSessionActivityRecord succinctDescriptionBuilder];
-[_UIViewServiceSessionActivityRecord init];
-[_UIViewServiceSessionActivityRecord descriptionWithMultilinePrefix:];
-[_UIViewServiceSessionActivityRecord succinctDescription];
-[_UIViewServiceSessionActivityRecord debugDescriptionWithMultilinePrefix:];
-[_UIViewServiceSessionActivityRecord description];
-[_UIViewServiceSessionActivityRecord descriptionBuilderWithMultilinePrefix:];
```
