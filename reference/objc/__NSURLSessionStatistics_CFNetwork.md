# `__NSURLSessionStatistics`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 6 properties, 11 instance methods, 2 class methods

## Instance variables

```
^v report;
@"NSMutableDictionary" _dictionaryReport;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N) dictionaryReport;
@property (T@"NSUUID",R,N) nwActivity;
@property (T@"NSUUID",R,N) taskUUID;
@property (T@"NSArray",R,N) connectionUUIDS;
@property (T@"NSUUID",&) externallyVisibleNwActivity;
@property (T@"NSArray",&) externallyVisibleConnectionUUIDs;
```

## Class methods

```
+[__NSURLSessionStatistics reportMetricsToSymptoms:];
+[__NSURLSessionStatistics createCFNetworkTaskMetrics_s:];
```

## Instance methods

```
-[__NSURLSessionStatistics taskUUID];
-[__NSURLSessionStatistics nwActivity];
-[__NSURLSessionStatistics dealloc];
-[__NSURLSessionStatistics initWithJSONData:];
-[__NSURLSessionStatistics dictionaryReport];
-[__NSURLSessionStatistics connectionUUIDS];
-[__NSURLSessionStatistics setExternallyVisibleNwActivity:];
-[__NSURLSessionStatistics initWithCFNetworkReport:length:];
-[__NSURLSessionStatistics externallyVisibleConnectionUUIDs];
-[__NSURLSessionStatistics externallyVisibleNwActivity];
-[__NSURLSessionStatistics setExternallyVisibleConnectionUUIDs:];
```
