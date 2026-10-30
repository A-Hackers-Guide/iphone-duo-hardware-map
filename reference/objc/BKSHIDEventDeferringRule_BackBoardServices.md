# `BKSHIDEventDeferringRule`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `NSCopying`, `NSSecureCoding`
- 7 instance variables, 10 properties, 19 instance methods, 5 class methods

## Instance variables

```
@"_BKSHIDEventDeferringRuleIdentity" _identity;
@"BKSHIDEventDeferringPredicate" _predicate;
@"NSSet" _restrictedToEventDescriptors;
@"BKSHIDEventDeferringTarget" _target;
@"NSString" _reason;
q _sortPriority;
q _priority;
```

## Properties

```
@property (T@"BKSHIDEventDeferringPredicate",R,C,N,V_predicate) predicate;
@property (T@"BKSHIDEventDeferringTarget",R,C,N,V_target) target;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (Tq,R,N,V_priority) priority;
@property (T@"_BKSHIDEventDeferringRuleIdentity",R,C,N,V_identity) identity;
@property (T@"NSSet",R,C,N,V_restrictedToEventDescriptors) restrictedToEventDescriptors;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringRule supportsSecureCoding];
+[BKSHIDEventDeferringRule ruleForDeferringEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:priority:seed:pid:];
+[BKSHIDEventDeferringRule ruleForDeferringEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:seed:pid:];
+[BKSHIDEventDeferringRule ruleForDeferringEventsMatchingPredicate:toTarget:withReason:priority:seed:pid:];
+[BKSHIDEventDeferringRule ruleForDeferringEventsMatchingPredicate:toTarget:withReason:seed:pid:];
```

## Instance methods

```
-[BKSHIDEventDeferringRule eventDescriptorIsRestricted:];
-[BKSHIDEventDeferringRule priority];
-[BKSHIDEventDeferringRule _initWithPredicate:restrictedToEventDescriptors:target:reason:identity:];
-[BKSHIDEventDeferringRule _initWithPredicate:restrictedToEventDescriptors:target:reason:priority:identity:];
-[BKSHIDEventDeferringRule init];
-[BKSHIDEventDeferringRule mostRecentFirstCompare:];
-[BKSHIDEventDeferringRule appendDescriptionToFormatter:];
-[BKSHIDEventDeferringRule restrictedToEventDescriptors];
-[BKSHIDEventDeferringRule weightedDeferringRuleCompare:];
-[BKSHIDEventDeferringRule encodeWithCoder:];
-[BKSHIDEventDeferringRule hash];
-[BKSHIDEventDeferringRule identity];
-[BKSHIDEventDeferringRule description];
-[BKSHIDEventDeferringRule initWithCoder:];
-[BKSHIDEventDeferringRule predicate];
-[BKSHIDEventDeferringRule reason];
-[BKSHIDEventDeferringRule target];
-[BKSHIDEventDeferringRule copyWithZone:];
-[BKSHIDEventDeferringRule isEqual:];
```
