# `BKSHIDEventSenderSpecificDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventDescriptor`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
Q _senderID;
@"BKSHIDEventDescriptor" _sourceDescriptor;
```

## Properties

```
@property (T@"BKSHIDEventDescriptor",&,N,V_sourceDescriptor) sourceDescriptor;
@property (TQ,R,V_senderID) senderID;
```

## Class methods

```
+[BKSHIDEventSenderSpecificDescriptor supportsSecureCoding];
```

## Instance methods

```
-[BKSHIDEventSenderSpecificDescriptor setSourceDescriptor:];
-[BKSHIDEventSenderSpecificDescriptor describes:];
-[BKSHIDEventSenderSpecificDescriptor senderID];
-[BKSHIDEventSenderSpecificDescriptor matchesHIDEvent:];
-[BKSHIDEventSenderSpecificDescriptor encodeWithCoder:];
-[BKSHIDEventSenderSpecificDescriptor requiresFuzzyMatching];
-[BKSHIDEventSenderSpecificDescriptor initWithCoder:];
-[BKSHIDEventSenderSpecificDescriptor appendDescriptionToStream:];
-[BKSHIDEventSenderSpecificDescriptor sourceDescriptor];
-[BKSHIDEventSenderSpecificDescriptor initWithDescriptor:senderID:];
-[BKSHIDEventSenderSpecificDescriptor descriptorByAddingSenderIDToMatchCriteria:];
```
