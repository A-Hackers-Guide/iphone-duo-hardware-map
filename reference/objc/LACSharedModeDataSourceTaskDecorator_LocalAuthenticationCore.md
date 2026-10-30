# `LACSharedModeDataSourceTaskDecorator`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACSharedModeDataSource`
- 3 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<LACSharedModeDataSource>" _dataSource;
@"LACSharedModeDataSourceTaskDecoratorRuntime" _runtime;
@"NSObject<OS_dispatch_queue>" _replyQueue;
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
-[LACSharedModeDataSourceTaskDecorator _sharedModeBackgroundTaskWithOptions:];
-[LACSharedModeDataSourceTaskDecorator _sharedModeFromBackgroundTaskResult:];
-[LACSharedModeDataSourceTaskDecorator _timeoutForRequestWithOptions:];
-[LACSharedModeDataSourceTaskDecorator fetchSharedModeWithOptions:completion:];
-[LACSharedModeDataSourceTaskDecorator initWithDataSource:replyQueue:];
-[LACSharedModeDataSourceTaskDecorator initWithDataSource:runtime:replyQueue:];
```
