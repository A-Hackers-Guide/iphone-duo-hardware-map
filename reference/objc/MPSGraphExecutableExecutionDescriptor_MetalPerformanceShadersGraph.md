# `MPSGraphExecutableExecutionDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 32 instance variables, 26 properties, 58 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _waitEvents;
@"NSMutableArray" _signalEvents;
@"NSMutableArray" _anePowerWaitEvents;
@? _profilingCallback;
@"NSMutableDictionary" _profilingDictionary;
Q _profilingBitmap;
Q _numberOfCommitsByMPSGraph;
B _waitUntilCompleted;
B _enableCommitAndContinue;
B _simulateANECompileFailure;
B _simulateANELoadModelFailure;
B _disableSynchronizeResults;
B _disableANECaching;
B _disableANEFallback;
B _enableProfilingOpNames;
B _briefProfilingOpNames;
B _breakUpMetalEncoders;
B _compilationOnly;
B _generateRuntimeExecutionReport;
B _encodeANESync;
B _encodeANEDisableSharedEvents;
B _assumeImmutableCompilationDescriptor;
@"NSSet" _intermediates;
@"NSDictionary" _intermediateResultIndices;
@? _scheduledHandler;
@? _completionHandler;
@? _scheduledGraphHandler;
@? _completionGraphHandler;
Q _maximumNumberOfEncodingThreads;
@"NSString" _entryFunctionName;
@"MPSGraphExecutableEntryPointToSymbolAndFileNameMap" _perEntryPointToSymbolAndFileNameMap;
Q _aneProcedureExecutionMode;
```

## Properties

```
@property (TB,V_enableCommitAndContinue) enableCommitAndContinue;
@property (T@?,C,V_scheduledGraphHandler) scheduledGraphHandler;
@property (T@?,C,V_completionGraphHandler) completionGraphHandler;
@property (TB,V_simulateANECompileFailure) simulateANECompileFailure;
@property (TB,V_simulateANELoadModelFailure) simulateANELoadModelFailure;
@property (TB,V_disableSynchronizeResults) disableSynchronizeResults;
@property (TB,V_disableANECaching) disableANECaching;
@property (TB,V_disableANEFallback) disableANEFallback;
@property (TB,V_enableProfilingOpNames) enableProfilingOpNames;
@property (TB,V_briefProfilingOpNames) briefProfilingOpNames;
@property (TB,V_breakUpMetalEncoders) breakUpMetalEncoders;
@property (TB,V_compilationOnly) compilationOnly;
@property (TB,V_generateRuntimeExecutionReport) generateRuntimeExecutionReport;
@property (TQ,V_maximumNumberOfEncodingThreads) maximumNumberOfEncodingThreads;
@property (TQ,R,V_numberOfCommitsByMPSGraph) numberOfCommitsByMPSGraph;
@property (T@"NSString",&,V_entryFunctionName) entryFunctionName;
@property (T@"MPSGraphExecutableEntryPointToSymbolAndFileNameMap",&,V_perEntryPointToSymbolAndFileNameMap) perEntryPointToSymbolAndFileNameMap;
@property (TQ,V_aneProcedureExecutionMode) aneProcedureExecutionMode;
@property (TB,V_encodeANESync) encodeANESync;
@property (TB,V_encodeANEDisableSharedEvents) encodeANEDisableSharedEvents;
@property (TB,V_assumeImmutableCompilationDescriptor) assumeImmutableCompilationDescriptor;
@property (T@"NSSet",&,V_intermediates) intermediates;
@property (T@"NSDictionary",&,V_intermediateResultIndices) intermediateResultIndices;
@property (T@?,C,V_scheduledHandler) scheduledHandler;
@property (T@?,C,V_completionHandler) completionHandler;
@property (TB,V_waitUntilCompleted) waitUntilCompleted;
```

## Instance methods

```
-[MPSGraphExecutableExecutionDescriptor waitUntilCompleted];
-[MPSGraphExecutableExecutionDescriptor setCompletionHandler:];
-[MPSGraphExecutableExecutionDescriptor completionHandler];
-[MPSGraphExecutableExecutionDescriptor init];
-[MPSGraphExecutableExecutionDescriptor copyWithZone:];
-[MPSGraphExecutableExecutionDescriptor waitForEvent:value:];
-[MPSGraphExecutableExecutionDescriptor perEntryPointToSymbolAndFileNameMap];
-[MPSGraphExecutableExecutionDescriptor requestProfilingStatsWithDictionary:profilingCallback:];
-[MPSGraphExecutableExecutionDescriptor setBreakUpMetalEncoders:];
-[MPSGraphExecutableExecutionDescriptor setBriefProfilingOpNames:];
-[MPSGraphExecutableExecutionDescriptor setEnableProfilingOpNames:];
-[MPSGraphExecutableExecutionDescriptor setEntryFunctionName:];
-[MPSGraphExecutableExecutionDescriptor setMaximumNumberOfEncodingThreads:];
-[MPSGraphExecutableExecutionDescriptor setPerEntryPointToSymbolAndFileNameMap:];
-[MPSGraphExecutableExecutionDescriptor setScheduledHandler:];
-[MPSGraphExecutableExecutionDescriptor setWaitUntilCompleted:];
-[MPSGraphExecutableExecutionDescriptor setAneProcedureExecutionMode:];
-[MPSGraphExecutableExecutionDescriptor setEnableCommitAndContinue:];
-[MPSGraphExecutableExecutionDescriptor signalEvent:atExecutionEvent:value:];
-[MPSGraphExecutableExecutionDescriptor waitForANEPrePowerUpEvent:value:];
-[MPSGraphExecutableExecutionDescriptor intermediates];
-[MPSGraphExecutableExecutionDescriptor scheduledHandler];
-[MPSGraphExecutableExecutionDescriptor compilationOnly];
-[MPSGraphExecutableExecutionDescriptor setSimulateANELoadModelFailure:];
-[MPSGraphExecutableExecutionDescriptor aneProcedureExecutionMode];
-[MPSGraphExecutableExecutionDescriptor assumeImmutableCompilationDescriptor];
-[MPSGraphExecutableExecutionDescriptor breakUpMetalEncoders];
-[MPSGraphExecutableExecutionDescriptor briefProfilingOpNames];
-[MPSGraphExecutableExecutionDescriptor completionGraphHandler];
-[MPSGraphExecutableExecutionDescriptor disableANECaching];
-[MPSGraphExecutableExecutionDescriptor disableANEFallback];
-[MPSGraphExecutableExecutionDescriptor disableSynchronizeResults];
-[MPSGraphExecutableExecutionDescriptor enableCommitAndContinue];
-[MPSGraphExecutableExecutionDescriptor enableProfilingOpNames];
-[MPSGraphExecutableExecutionDescriptor encodeANEDisableSharedEvents];
-[MPSGraphExecutableExecutionDescriptor encodeANESync];
-[MPSGraphExecutableExecutionDescriptor entryFunctionName];
-[MPSGraphExecutableExecutionDescriptor generateRuntimeExecutionReport];
-[MPSGraphExecutableExecutionDescriptor initWithGraphExecutionDescriptor:];
-[MPSGraphExecutableExecutionDescriptor intermediateResultIndices];
-[MPSGraphExecutableExecutionDescriptor maximumNumberOfEncodingThreads];
-[MPSGraphExecutableExecutionDescriptor numberOfCommitsByMPSGraph];
-[MPSGraphExecutableExecutionDescriptor scheduledGraphHandler];
-[MPSGraphExecutableExecutionDescriptor setAssumeImmutableCompilationDescriptor:];
-[MPSGraphExecutableExecutionDescriptor setCompilationOnly:];
-[MPSGraphExecutableExecutionDescriptor setCompletionGraphHandler:];
-[MPSGraphExecutableExecutionDescriptor setDisableANECaching:];
-[MPSGraphExecutableExecutionDescriptor setDisableANEFallback:];
-[MPSGraphExecutableExecutionDescriptor setDisableSynchronizeResults:];
-[MPSGraphExecutableExecutionDescriptor setEncodeANEDisableSharedEvents:];
-[MPSGraphExecutableExecutionDescriptor setEncodeANESync:];
-[MPSGraphExecutableExecutionDescriptor setGenerateRuntimeExecutionReport:];
-[MPSGraphExecutableExecutionDescriptor setIntermediateResultIndices:];
-[MPSGraphExecutableExecutionDescriptor setIntermediates:];
-[MPSGraphExecutableExecutionDescriptor setScheduledGraphHandler:];
-[MPSGraphExecutableExecutionDescriptor setSimulateANECompileFailure:];
-[MPSGraphExecutableExecutionDescriptor simulateANECompileFailure];
-[MPSGraphExecutableExecutionDescriptor simulateANELoadModelFailure];
```
