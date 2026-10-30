# `PPSSignpostController`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"PPSSignpostServiceConnection" _connection;
```

## Properties

```
@property (T@"PPSSignpostServiceConnection",&,V_connection) connection;
```

## Class methods

```
+[PPSSignpostController _workQueue];
+[PPSSignpostController registerDataCollectionActivity];
+[PPSSignpostController unregisterDataCollectionActivity];
```

## Instance methods

```
-[PPSSignpostController _clearState];
-[PPSSignpostController init];
-[PPSSignpostController connection];
-[PPSSignpostController setConnection:];
-[PPSSignpostController _handleTask:];
-[PPSSignpostController _lastCollectionDate];
-[PPSSignpostController _performWithStartDate:endDate:];
-[PPSSignpostController generateForTimeRange:];
```
