# `MPSGraphExecutionDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 18 instance variables, 15 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _waitEvents;
@"NSMutableArray" _signalEvents;
@"NSMutableArray" _anePowerWaitEvents;
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
B _generateRuntimeExecutionReport;
@"MPSGraphCompilationDescriptor" _compilationDescriptor;
@? _scheduledHandler;
@? _completionHandler;
Q _maximumNumberOfEncodingThreads;
```

## Properties

```
@property (TB,V_enableCommitAndContinue) enableCommitAndContinue;
@property (TB,V_simulateANECompileFailure) simulateANECompileFailure;
@property (TB,V_simulateANELoadModelFailure) simulateANELoadModelFailure;
@property (TB,V_disableSynchronizeResults) disableSynchronizeResults;
@property (TB,V_disableANECaching) disableANECaching;
@property (TB,V_disableANEFallback) disableANEFallback;
@property (TB,V_enableProfilingOpNames) enableProfilingOpNames;
@property (TB,V_briefProfilingOpNames) briefProfilingOpNames;
@property (TB,V_breakUpMetalEncoders) breakUpMetalEncoders;
@property (TB,V_generateRuntimeExecutionReport) generateRuntimeExecutionReport;
@property (TQ,V_maximumNumberOfEncodingThreads) maximumNumberOfEncodingThreads;
@property (T@?,C,V_scheduledHandler) scheduledHandler;
@property (T@?,C,V_completionHandler) completionHandler;
@property (TB,V_waitUntilCompleted) waitUntilCompleted;
@property (T@"MPSGraphCompilationDescriptor",C,V_compilationDescriptor) compilationDescriptor;
```

## Instance methods

```
-[MPSGraphExecutionDescriptor waitUntilCompleted];
-[MPSGraphExecutionDescriptor setCompletionHandler:];
-[MPSGraphExecutionDescriptor completionHandler];
-[MPSGraphExecutionDescriptor init];
-[MPSGraphExecutionDescriptor waitForEvent:value:];
-[MPSGraphExecutionDescriptor compilationDescriptor];
-[MPSGraphExecutionDescriptor setBreakUpMetalEncoders:];
-[MPSGraphExecutionDescriptor setBriefProfilingOpNames:];
-[MPSGraphExecutionDescriptor setCompilationDescriptor:];
-[MPSGraphExecutionDescriptor setEnableProfilingOpNames:];
-[MPSGraphExecutionDescriptor setMaximumNumberOfEncodingThreads:];
-[MPSGraphExecutionDescriptor setScheduledHandler:];
-[MPSGraphExecutionDescriptor setWaitUntilCompleted:];
-[MPSGraphExecutionDescriptor setEnableCommitAndContinue:];
-[MPSGraphExecutionDescriptor signalEvent:atExecutionEvent:value:];
-[MPSGraphExecutionDescriptor waitForANEPrePowerUpEvent:value:];
-[MPSGraphExecutionDescriptor scheduledHandler];
-[MPSGraphExecutionDescriptor setSimulateANELoadModelFailure:];
-[MPSGraphExecutionDescriptor breakUpMetalEncoders];
-[MPSGraphExecutionDescriptor briefProfilingOpNames];
-[MPSGraphExecutionDescriptor disableANECaching];
-[MPSGraphExecutionDescriptor disableANEFallback];
-[MPSGraphExecutionDescriptor disableSynchronizeResults];
-[MPSGraphExecutionDescriptor enableCommitAndContinue];
-[MPSGraphExecutionDescriptor enableProfilingOpNames];
-[MPSGraphExecutionDescriptor generateRuntimeExecutionReport];
-[MPSGraphExecutionDescriptor maximumNumberOfEncodingThreads];
-[MPSGraphExecutionDescriptor setDisableANECaching:];
-[MPSGraphExecutionDescriptor setDisableANEFallback:];
-[MPSGraphExecutionDescriptor setDisableSynchronizeResults:];
-[MPSGraphExecutionDescriptor setGenerateRuntimeExecutionReport:];
-[MPSGraphExecutionDescriptor setSimulateANECompileFailure:];
-[MPSGraphExecutionDescriptor simulateANECompileFailure];
-[MPSGraphExecutionDescriptor simulateANELoadModelFailure];
```
