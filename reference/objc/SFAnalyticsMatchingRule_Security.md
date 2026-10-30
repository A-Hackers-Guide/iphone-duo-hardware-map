# `SFAnalyticsMatchingRule`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _firstMatchArmed;
@"NSString" _eventName;
@"SECSFAEventRule" _rule;
@"NSDictionary" _matchingDictionary;
@"NSDate" _lastMatch;
```

## Properties

```
@property (T@"SECSFAEventRule",&,V_rule) rule;
@property (T@"NSDictionary",&,V_matchingDictionary) matchingDictionary;
@property (T@"NSDate",&,V_lastMatch) lastMatch;
@property (TB,V_firstMatchArmed) firstMatchArmed;
@property (T@"NSString",&,V_eventName) eventName;
```

## Class methods

```
+[SFAnalyticsMatchingRule armKeyForEventName:];
```

## Instance methods

```
-[SFAnalyticsMatchingRule rule];
-[SFAnalyticsMatchingRule eventName];
-[SFAnalyticsMatchingRule description];
-[SFAnalyticsMatchingRule firstMatchArmed];
-[SFAnalyticsMatchingRule armKey];
-[SFAnalyticsMatchingRule cachedMatchDictionary];
-[SFAnalyticsMatchingRule doAction:attributes:logger:];
-[SFAnalyticsMatchingRule initWithSFARule:logger:];
-[SFAnalyticsMatchingRule isSubsetMatch:target:];
-[SFAnalyticsMatchingRule lastMatch];
-[SFAnalyticsMatchingRule lastMatchTimeKey];
-[SFAnalyticsMatchingRule matchAttributes:eventClass:processName:logger:];
-[SFAnalyticsMatchingRule matchingDictionary];
-[SFAnalyticsMatchingRule setEventName:];
-[SFAnalyticsMatchingRule setFirstMatchArmed:];
-[SFAnalyticsMatchingRule setLastMatch:];
-[SFAnalyticsMatchingRule setMatchingDictionary:];
-[SFAnalyticsMatchingRule setRule:];
-[SFAnalyticsMatchingRule valueMatch:target:];
```
