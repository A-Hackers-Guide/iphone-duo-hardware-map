# `_SBFKeyWindowStack`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"SBFWindow" _expectedKeyWindow;
@"NSMutableOrderedSet" _windowStack;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_SBFKeyWindowStack sharedInstance];
```

## Instance methods

```
-[_SBFKeyWindowStack _keyWindowDidChangeNotification:];
-[_SBFKeyWindowStack _isWindowEligibleForKeyness:];
-[_SBFKeyWindowStack succinctDescriptionBuilder];
-[_SBFKeyWindowStack init];
-[_SBFKeyWindowStack dealloc];
-[_SBFKeyWindowStack expectedKeyWindow];
-[_SBFKeyWindowStack descriptionWithMultilinePrefix:];
-[_SBFKeyWindowStack popKeyWindow:reason:];
-[_SBFKeyWindowStack succinctDescription];
-[_SBFKeyWindowStack popKeyWindow:];
-[_SBFKeyWindowStack _evaluateForNewKeyWindowWithReason:];
-[_SBFKeyWindowStack noteWindowHidden:];
-[_SBFKeyWindowStack noteWindowUnhidden:];
-[_SBFKeyWindowStack description];
-[_SBFKeyWindowStack pushKeyWindow:];
-[_SBFKeyWindowStack noteWindowDeallocated:];
-[_SBFKeyWindowStack descriptionBuilderWithMultilinePrefix:];
```
