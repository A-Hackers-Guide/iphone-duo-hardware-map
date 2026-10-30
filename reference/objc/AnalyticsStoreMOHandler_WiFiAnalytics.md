# `AnalyticsStoreMOHandler`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"WAPersistentContainer" _persistentContainer;
@"NSManagedObjectContext" _backgroundStoreMoHandlerMOC;
```

## Properties

```
@property (T@"WAPersistentContainer",&,N,V_persistentContainer) persistentContainer;
@property (T@"NSManagedObjectContext",&,N,V_backgroundStoreMoHandlerMOC) backgroundStoreMoHandlerMOC;
```

## Class methods

```
+[AnalyticsStoreMOHandler sharedAnalyticsStoreMOHandlerWithContainer:];
```

## Instance methods

```
-[AnalyticsStoreMOHandler managedObjectContext];
-[AnalyticsStoreMOHandler managedObjectContextSave:reset:release:withError:];
-[AnalyticsStoreMOHandler setPersistentContainer:];
-[AnalyticsStoreMOHandler dealloc];
-[AnalyticsStoreMOHandler initWithContainer:];
-[AnalyticsStoreMOHandler releaseBackgroundMOC];
-[AnalyticsStoreMOHandler persistentContainer];
-[AnalyticsStoreMOHandler saveManagedObjectContextWithError:];
-[AnalyticsStoreMOHandler resetManagedObjectContext];
-[AnalyticsStoreMOHandler contextDidSave:];
-[AnalyticsStoreMOHandler setBackgroundStoreMoHandlerMOC:];
-[AnalyticsStoreMOHandler backgroundStoreMoHandlerMOC];
-[AnalyticsStoreMOHandler performBlockOnManagedObjectContext:block:];
-[AnalyticsStoreMOHandler performBlockOnManagedObjectContextForNSData:withDate:block:];
-[AnalyticsStoreMOHandler setBssManagedObjectPropertyValueForKeyWithoutSave:forKey:withValue:];
-[AnalyticsStoreMOHandler setNetworkManagedObjectPropertyValueForKeyWithoutSave:forKey:withValue:];
-[AnalyticsStoreMOHandler updateManagedObjectContextWithoutSave];
```
