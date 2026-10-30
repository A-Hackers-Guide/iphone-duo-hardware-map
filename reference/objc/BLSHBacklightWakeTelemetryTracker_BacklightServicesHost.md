# `BLSHBacklightWakeTelemetryTracker`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 32 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{vm_statistics64="free_count"I"active_count"I"inactive_count"I"wire_count"I"zero_fill_count"Q"reactivations"Q"pageins"Q"pageouts"Q"faults"Q"cow_faults"Q"lookups"Q"hits"Q"purges"Q"purgeable_count"I"speculative_count"I"decompressions"Q"compressions"Q"swapins"Q"swapouts"Q"compressor_page_count"I"throttled_count"I"external_page_count"I"internal_page_count"I"total_uncompressed_pages_in_compressor"Q"swapped_count"Q"total_tag_storage_pages"Q"nontag_pageable_tag_storage_pages"Q"nontag_wired_tag_storage_pages"Q"free_tag_storage_pages"Q"tag_storing_tag_storage_pages"Q"total_tagged_pages"Q"resident_tagged_pages"Q"compressed_tagged_pages"Q"tagged_compressions"Q"tagged_decompressions"Q"compressed_tag_storage_bytes"Q"speculative_pages_created"Q"speculative_pages_activated"Q"swap_count"Q"empty_tag_storing_tag_storage_pages"Q"executable_count"Q"shared_region_count"Q"boot_stolen_count"Q"secluded_count"Q"active_internal_count"Q"inactive_internal_count"Q"active_external_count"Q"inactive_external_count"Q"purgeable_pageable_count"Q"purgeable_wired_count"Q"background_internal_count"Q"background_external_count"Q"donated_count"Q"realtime_count"Q"max_mem_count"Q"phantom_ghosts_found"Q"phantom_ghosts_added"Q} _lock_vmStatsBegin;
{vm_statistics64="free_count"I"active_count"I"inactive_count"I"wire_count"I"zero_fill_count"Q"reactivations"Q"pageins"Q"pageouts"Q"faults"Q"cow_faults"Q"lookups"Q"hits"Q"purges"Q"purgeable_count"I"speculative_count"I"decompressions"Q"compressions"Q"swapins"Q"swapouts"Q"compressor_page_count"I"throttled_count"I"external_page_count"I"internal_page_count"I"total_uncompressed_pages_in_compressor"Q"swapped_count"Q"total_tag_storage_pages"Q"nontag_pageable_tag_storage_pages"Q"nontag_wired_tag_storage_pages"Q"free_tag_storage_pages"Q"tag_storing_tag_storage_pages"Q"total_tagged_pages"Q"resident_tagged_pages"Q"compressed_tagged_pages"Q"tagged_compressions"Q"tagged_decompressions"Q"compressed_tag_storage_bytes"Q"speculative_pages_created"Q"speculative_pages_activated"Q"swap_count"Q"empty_tag_storing_tag_storage_pages"Q"executable_count"Q"shared_region_count"Q"boot_stolen_count"Q"secluded_count"Q"active_internal_count"Q"inactive_internal_count"Q"active_external_count"Q"inactive_external_count"Q"purgeable_pageable_count"Q"purgeable_wired_count"Q"background_internal_count"Q"background_external_count"Q"donated_count"Q"realtime_count"Q"max_mem_count"Q"phantom_ghosts_found"Q"phantom_ghosts_added"Q} _lock_vmStatsPendingEnd;
@"<SWSystemActivityAcquisitionDetails>" _lock_systemActivityDetails;
Q _lock_pendingEndTime;
Q _lock_pendingEndpoint;
@"BLSBacklightChangeEvent" _lock_initialEvent;
@"BLSBacklightChangeEvent" _lock_triggerEvent;
@"BLSBacklightChangeEvent" _lock_lastEvent;
@? _lock_completion;
@"BLSHMeasureCommitOnWakeOperation" _measureCommitOnWakeOperation;
Q _lock_beginMachTime;
d _lock_didCompleteDurationSeconds;
d _lock_systemActivityAcquisitionSeconds;
d _lock_secondsAfterKernelWake;
i _lock_performEventCounter;
i _lock_completedEventsCount;
i _lock_abortedEventsCount;
B _lock_didBegin;
B _lock_didUnblank;
B _lock_didCompleteUpdate;
B _lock_didMeasure;
B _lock_didAcquireSystemActivity;
B _lock_hadExistingSystemActivity;
B _lock_didTimeout;
B _lock_invalidated;
B _lock_completionPending;
B _lock_commitOnWakeMeasurementDisabled;
B _lock_beforeKernelWake;
B _lock_systemActivitySuccess;
B _lock_systemActivityDidTimeout;
B _lock_timeoutTriggeredBlackFlash;
```

## Properties

```
@property (TB,N,GisCommitOnWakeMeasurementDisabled) commitOnWakeMeasurementDisabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHBacklightWakeTelemetryTracker init];
-[BLSHBacklightWakeTelemetryTracker dealloc];
-[BLSHBacklightWakeTelemetryTracker invalidate];
-[BLSHBacklightWakeTelemetryTracker _lock_checkAgainstTriggerEvent:];
-[BLSHBacklightWakeTelemetryTracker _lock_captureStatsForPendingEndpoint:timestamp:];
-[BLSHBacklightWakeTelemetryTracker beginForEvent:completion:];
-[BLSHBacklightWakeTelemetryTracker checkCompleteForEvent:];
-[BLSHBacklightWakeTelemetryTracker completeForEvent:];
-[BLSHBacklightWakeTelemetryTracker didAcquireSystemActivityWithError:isActive:details:forEvent:];
-[BLSHBacklightWakeTelemetryTracker didCompleteUpdateForEvents:abortedEvents:];
-[BLSHBacklightWakeTelemetryTracker didUnblankForEvents:];
-[BLSHBacklightWakeTelemetryTracker didUpdateVisualContentsToBeginTransitionToActiveOnForEvent:];
-[BLSHBacklightWakeTelemetryTracker hadExistingSystemActivityForEvent:];
-[BLSHBacklightWakeTelemetryTracker incrementPerformEventCounterWithEvent:];
-[BLSHBacklightWakeTelemetryTracker isCommitOnWakeMeasurementDisabled];
-[BLSHBacklightWakeTelemetryTracker setCommitOnWakeMeasurementDisabled:];
-[BLSHBacklightWakeTelemetryTracker willUnblankForEvent:];
```
