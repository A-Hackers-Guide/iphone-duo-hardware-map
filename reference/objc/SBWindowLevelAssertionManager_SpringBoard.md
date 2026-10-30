# `SBWindowLevelAssertionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<SBWindowLevelAssertionManagerDelegate>" _delegate;
@"NSMapTable" _windowLevelAssertionsPerScene;
```

## Properties

```
@property (T@"NSMapTable",R,N,V_windowLevelAssertionsPerScene) windowLevelAssertionsPerScene;
@property (T@"<SBWindowLevelAssertionManagerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowLevelAssertionManager acquireWindowLevelAssertionWithPriority:windowLevel:windowScene:reason:];
-[SBWindowLevelAssertionManager debugDescription];
-[SBWindowLevelAssertionManager succinctDescriptionBuilder];
-[SBWindowLevelAssertionManager init];
-[SBWindowLevelAssertionManager descriptionWithMultilinePrefix:];
-[SBWindowLevelAssertionManager succinctDescription];
-[SBWindowLevelAssertionManager setDelegate:];
-[SBWindowLevelAssertionManager delegate];
-[SBWindowLevelAssertionManager description];
-[SBWindowLevelAssertionManager descriptionBuilderWithMultilinePrefix:];
-[SBWindowLevelAssertionManager _notifyDelegateAssertionsDidUpdateForWindowScene:];
-[SBWindowLevelAssertionManager highestPriorityWindowLevelAssertionForWindowScene:];
-[SBWindowLevelAssertionManager windowLevelAssertionsPerScene];
```
