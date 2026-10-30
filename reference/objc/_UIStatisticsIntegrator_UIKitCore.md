# `_UIStatisticsIntegrator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _reportingQueue;
```

## Class methods

```
+[_UIStatisticsIntegrator sharedInstance];
+[_UIStatisticsIntegrator setSharedInstance:];
+[_UIStatisticsIntegrator createSharedInstanceIfNecessary];
```

## Instance methods

```
-[_UIStatisticsIntegrator resetDistributionForKey:];
-[_UIStatisticsIntegrator incrementValueBy:forKey:];
-[_UIStatisticsIntegrator init];
-[_UIStatisticsIntegrator batchRecord:];
-[_UIStatisticsIntegrator recordDistributionValue:forKey:];
-[_UIStatisticsIntegrator recordDistributionTime:forKey:];
-[_UIStatisticsIntegrator setValue:forKey:];
-[_UIStatisticsIntegrator resetDistributionToValue:forKey:];
-[_UIStatisticsIntegrator resetValueForKey:];
```
