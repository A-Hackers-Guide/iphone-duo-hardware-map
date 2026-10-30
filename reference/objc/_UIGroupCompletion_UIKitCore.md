# `_UIGroupCompletion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIGroupCompletionProviding`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _completions;
@"NSMutableArray" _scheduledCompletions;
Q _refCount;
B _isCompleting;
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
-[_UIGroupCompletion addCompletion:];
-[_UIGroupCompletion _performAllCompletions];
-[_UIGroupCompletion increment];
-[_UIGroupCompletion complete];
-[_UIGroupCompletion addNonIncrementingCompletion:];
-[_UIGroupCompletion completeImmediately];
-[_UIGroupCompletion replaceCompletion:];
```
