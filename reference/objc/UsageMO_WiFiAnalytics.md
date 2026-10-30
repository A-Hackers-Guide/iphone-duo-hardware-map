# `UsageMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UniqueMO`
- Protocols: `UniqueMoProtocol`
- 0 instance variables, 4 properties, 1 instance methods, 12 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UsageMO accumulator];
+[UsageMO verifyConstraints:withError:];
+[UsageMO timeSpan];
+[UsageMO jumpBackOneSpan];
+[UsageMO aggregateAs];
+[UsageMO aggregateName];
+[UsageMO binnedValue:inEdges:withLowerEdgeIncluded:];
+[UsageMO checkForInvalid:constraint:on:];
+[UsageMO constraintsWithBss:date:lqm:onEntity:];
+[UsageMO datedProperty];
+[UsageMO referenceDateFor:timeSpan:withError:];
+[UsageMO usageOf:timeSpan:around:onContainer:withError:];
```

## Instance methods

```
-[UsageMO description];
```
