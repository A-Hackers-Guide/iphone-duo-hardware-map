# `BKSHIDEventDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSSecureCoding`, `BSDescriptionProviding`, `NSCopying`
- 1 instance variables, 5 properties, 20 instance methods, 4 class methods

## Instance variables

```
I _hidEventType;
```

## Properties

```
@property (TI,R,N,V_hidEventType) hidEventType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDescriptor supportsSecureCoding];
+[BKSHIDEventDescriptor appendDescriptorArray:toDescriptionStream:];
+[BKSHIDEventDescriptor descriptorForHIDEvent:];
+[BKSHIDEventDescriptor descriptorWithEventType:];
```

## Instance methods

```
-[BKSHIDEventDescriptor succinctDescriptionBuilder];
-[BKSHIDEventDescriptor compare:];
-[BKSHIDEventDescriptor init];
-[BKSHIDEventDescriptor hidEventType];
-[BKSHIDEventDescriptor describes:];
-[BKSHIDEventDescriptor descriptionWithMultilinePrefix:];
-[BKSHIDEventDescriptor succinctDescription];
-[BKSHIDEventDescriptor _initWithEventType:];
-[BKSHIDEventDescriptor matchesHIDEvent:];
-[BKSHIDEventDescriptor initWithEventType:];
-[BKSHIDEventDescriptor encodeWithCoder:];
-[BKSHIDEventDescriptor hash];
-[BKSHIDEventDescriptor requiresFuzzyMatching];
-[BKSHIDEventDescriptor description];
-[BKSHIDEventDescriptor initWithCoder:];
-[BKSHIDEventDescriptor appendDescriptionToStream:];
-[BKSHIDEventDescriptor copyWithZone:];
-[BKSHIDEventDescriptor isEqual:];
-[BKSHIDEventDescriptor descriptorByAddingSenderIDToMatchCriteria:];
-[BKSHIDEventDescriptor descriptionBuilderWithMultilinePrefix:];
```
