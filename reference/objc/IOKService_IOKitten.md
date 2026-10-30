# `IOKService`

- Image: [`/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`](../userland/System__Library__PrivateFrameworks__IOKitten.framework__IOKitten.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOKRegistryEntry`
- 0 instance variables, 0 properties, 7 instance methods, 8 class methods

## Class methods

```
+[IOKService addNotificationOfType:forMatching:usingNotificationPort:error:withHandler:];
+[IOKService entryIDMatching:];
+[IOKService matchingService:];
+[IOKService matchingServices:error:];
+[IOKService serviceMatching:];
+[IOKService addNotificationOfType:forMatching:usingNotificationPort:error:withEnumerationBlock:];
+[IOKService bsdNameMatching:];
+[IOKService nameMatching:];
```

## Instance methods

```
-[IOKService busyState];
-[IOKService addInterestNotifcationOfType:usingNotificationPort:error:withHandler:];
-[IOKService requestProbeWithOptions:error:];
-[IOKService initWithServiceEntry:];
-[IOKService isServiceAuthorizedForOpenAllowInteraction:];
-[IOKService connectToServiceOfType:];
-[IOKService matchesPropertyTable:error:];
```
