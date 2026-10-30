# `BKSHIDEventUsagePairDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventDescriptor`
- 2 instance variables, 2 properties, 13 instance methods, 2 class methods

## Instance variables

```
I _page;
I _usage;
```

## Properties

```
@property (TI,R,V_page) page;
@property (TI,R,V_usage) usage;
```

## Class methods

```
+[BKSHIDEventUsagePairDescriptor supportsSecureCoding];
+[BKSHIDEventUsagePairDescriptor descriptorForHIDEventType:page:usage:];
```

## Instance methods

```
-[BKSHIDEventUsagePairDescriptor usage];
-[BKSHIDEventUsagePairDescriptor compare:];
-[BKSHIDEventUsagePairDescriptor describes:];
-[BKSHIDEventUsagePairDescriptor matchesHIDEvent:];
-[BKSHIDEventUsagePairDescriptor encodeWithCoder:];
-[BKSHIDEventUsagePairDescriptor page];
-[BKSHIDEventUsagePairDescriptor hash];
-[BKSHIDEventUsagePairDescriptor requiresFuzzyMatching];
-[BKSHIDEventUsagePairDescriptor initWithCoder:];
-[BKSHIDEventUsagePairDescriptor appendDescriptionToStream:];
-[BKSHIDEventUsagePairDescriptor _page:usage:matchesHIDEvent:];
-[BKSHIDEventUsagePairDescriptor _initWithPage:usage:eventType:];
-[BKSHIDEventUsagePairDescriptor isEqual:];
```
