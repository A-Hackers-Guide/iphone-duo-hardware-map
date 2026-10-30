# `TBPopularityScore`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBScore`
- 2 instance variables, 6 properties, 7 instance methods, 2 class methods

## Instance variables

```
Q _score;
@"NSString" _typeDescription;
```

## Properties

```
@property (T@"NSString",&,N,V_typeDescription) typeDescription;
@property (TQ,N,V_score) score;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBPopularityScore supportsSecureCoding];
+[TBPopularityScore popularityScoreWithValue:];
```

## Instance methods

```
-[TBPopularityScore setScore:];
-[TBPopularityScore score];
-[TBPopularityScore initWithValue:];
-[TBPopularityScore typeDescription];
-[TBPopularityScore encodeWithCoder:];
-[TBPopularityScore initWithCoder:];
-[TBPopularityScore setTypeDescription:];
```
