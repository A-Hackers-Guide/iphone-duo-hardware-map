# `UIWritingToolsCoordinatorAnimationParameters`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
d _delay;
d _duration;
@? _progressHandler;
@? _completionHandler;
```

## Properties

```
@property (Td,R,N,V_duration) duration;
@property (Td,R,N,V_delay) delay;
@property (T@?,C,N,V_progressHandler) progressHandler;
@property (T@?,C,N,V_completionHandler) completionHandler;
```

## Instance methods

```
-[UIWritingToolsCoordinatorAnimationParameters setProgressHandler:];
-[UIWritingToolsCoordinatorAnimationParameters progressHandler];
-[UIWritingToolsCoordinatorAnimationParameters setCompletionHandler:];
-[UIWritingToolsCoordinatorAnimationParameters completionHandler];
-[UIWritingToolsCoordinatorAnimationParameters duration];
-[UIWritingToolsCoordinatorAnimationParameters delay];
-[UIWritingToolsCoordinatorAnimationParameters initWithDelay:duration:];
```
