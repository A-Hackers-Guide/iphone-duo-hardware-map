# `SignpostReaderHelper`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _connectionToServer;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connectionToServer) connectionToServer;
```

## Class methods

```
+[SignpostReaderHelper extractStateIntervalsFromSignpostData:];
```

## Instance methods

```
-[SignpostReaderHelper closeXPCConnection];
-[SignpostReaderHelper connectionToServer];
-[SignpostReaderHelper setConnectionToServer:];
-[SignpostReaderHelper createXPCConnection];
-[SignpostReaderHelper customGetNearestMidnight];
-[SignpostReaderHelper generateRapidMSSWithStartDate:endDate:atPath:];
-[SignpostReaderHelper generateRapidSignpostSummaryWithStartDate:endDate:];
-[SignpostReaderHelper generateSignpostSubmissionWithTagConfig:withAllowlist:withStartDate:withEndDate:includeSPFile:];
-[SignpostReaderHelper generateTaskingMSSWithStartDate:endDate:atPath:];
-[SignpostReaderHelper getSignpostMetricsWithStartDate:withEndDate:processMXSignpost:collectStateIntervals:chunkIntervals:stateAwareClientsAllowlist:];
-[SignpostReaderHelper getSignpostSummaryWithAllowlist:withStartDate:withEndDate:];
-[SignpostReaderHelper processSignpostWithConfig:withServiceType:];
```
