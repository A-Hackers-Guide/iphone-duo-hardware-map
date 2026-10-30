# `WAEventDiagnosticState`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WAEvent`
- 4 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="band"s"channel"s"channelWidth"s"motionState"s"reason"i"rssi"s"status"i"subreason"i"enabled"B} _data;
@"NSString" _desc;
@"NSString" _name;
@"NSUUID" _uuid;
```

## Properties

```
@property (T@"NSString",&,N,V_desc) desc;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSUUID",&,N,V_uuid) uuid;
```

## Instance methods

```
-[WAEventDiagnosticState processEventOnPersistentContainer:andRunPostprocessing:withError:];
-[WAEventDiagnosticState updateRecord:];
-[WAEventDiagnosticState uuid];
-[WAEventDiagnosticState data];
-[WAEventDiagnosticState setUuid:];
-[WAEventDiagnosticState setDesc:];
-[WAEventDiagnosticState desc];
-[WAEventDiagnosticState description];
-[WAEventDiagnosticState setName:];
-[WAEventDiagnosticState initWithName:description:uuid:at:data:withLqmHistory:withError:];
-[WAEventDiagnosticState name];
```
