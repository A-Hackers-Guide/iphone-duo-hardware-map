# `BWLimitedGMErrorLogger`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
i _maxLoggingCount;
i _currentLoggingCount;
@"NSString" _name;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (Ti,R,N,V_maxLoggingCount) maxLoggingCount;
@property (Ti,R,N,V_currentLoggingCount) currentLoggingCount;
```

## Instance methods

```
-[BWLimitedGMErrorLogger dealloc];
-[BWLimitedGMErrorLogger name];
-[BWLimitedGMErrorLogger maxLoggingCount];
-[BWLimitedGMErrorLogger currentLoggingCount];
-[BWLimitedGMErrorLogger initWithName:maxLoggingCount:];
-[BWLimitedGMErrorLogger logErrorNumber:errorString:];
-[BWLimitedGMErrorLogger resetCurrentLoggingCounter];
```
