# `ANMigrationDependencyController`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
Q _liveImplementation;
B _isShadowModeEnabled;
@"NSString" _identifier;
d _timeout;
@"NSObject<OS_dispatch_queue>" _queue;
@? _isEqual;
@"ANSignalParityChecker" _signalParityChecker;
@? _onError;
```

## Properties

```
@property (T@?,C,N,V_onError) onError;
```

## Class methods

```
+[ANMigrationDependencyController runTestMode];
```

## Instance methods

```
-[ANMigrationDependencyController dealloc];
-[ANMigrationDependencyController onError];
-[ANMigrationDependencyController setOnError:];
-[ANMigrationDependencyController initWithLiveImplementation:isShadowModeEnabled:identifier:timeout:queue:getTimeIntervalSince1970:isEqual:];
-[ANMigrationDependencyController shouldLogForImplementation:];
-[ANMigrationDependencyController shouldRunImplementation:];
-[ANMigrationDependencyController shouldUseOutputFromImplementation:output:];
```
