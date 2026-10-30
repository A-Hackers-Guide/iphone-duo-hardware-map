# `CMNatalieData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 7 instance variables, 7 properties, 13 instance methods, 2 class methods

## Instance variables

```
q fRecordId;
d fStartDate;
q fActivityType;
d fMets;
d fNatalies;
d fBasalNatalies;
@"NSUUID" fSourceId;
```

## Properties

```
@property (Tq,R,N) recordId;
@property (T@"NSUUID",R,N) sourceId;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSNumber",R,N) mets;
@property (T@"NSNumber",R,N) natalies;
@property (T@"NSNumber",R,N) basalNatalies;
@property (Tq,R,N) activityType;
```

## Class methods

```
+[CMNatalieData supportsSecureCoding];
+[CMNatalieData maxNatalieEntries];
```

## Instance methods

```
-[CMNatalieData startDate];
-[CMNatalieData sourceId];
-[CMNatalieData recordId];
-[CMNatalieData dealloc];
-[CMNatalieData activityType];
-[CMNatalieData encodeWithCoder:];
-[CMNatalieData description];
-[CMNatalieData initWithCoder:];
-[CMNatalieData copyWithZone:];
-[CMNatalieData basalNatalies];
-[CMNatalieData initWithStartDate:recordId:activityType:mets:natalies:basalNatalies:sourceId:];
-[CMNatalieData mets];
-[CMNatalieData natalies];
```
