# `WAUtil`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 54 class methods

## Class methods

```
+[WAUtil isInternalInstall];
+[WAUtil getAWDTimestamp];
+[WAUtil trimTokenForLogging:];
+[WAUtil getLazyNSNumberPreference:domain:exists:];
+[WAUtil addDeltaNSNumberForTelemetryKey:dictKey:dictModule:telDict:recentDict:oldDict:];
+[WAUtil incrementValueForKey:inMutableDict:onQueue:];
+[WAUtil initialize];
+[WAUtil filterSet:usingPredicate:];
+[WAUtil isMacAddress:];
+[WAUtil storeToken:withIdentifier:];
+[WAUtil filterArray:usingPredicate:];
+[WAUtil groupTypeToString:];
+[WAUtil _generateInvocationForMethod:];
+[WAUtil mergeEventLists:ascending:];
+[WAUtil setPreference:domain:value:];
+[WAUtil filterArrayForKeys:];
+[WAUtil wifianalyticsTmpDirectory];
+[WAUtil getLazyNSStringPreference:domain:exists:];
+[WAUtil filterArrayForDottedKeyPaths:];
+[WAUtil isPreinstalledWiFiAppVisible];
+[WAUtil addFieldsForChannelFlagLikeKey:inDict:];
+[WAUtil setSamplingDisabledForTesting:];
+[WAUtil getValueForEntitlementForCurrentProcess:];
+[WAUtil getMessageInstanceForKey:andGroupType:];
+[WAUtil isWiFiAppInstalled];
+[WAUtil isAnalyticsStoreAllowed];
+[WAUtil canPerformActionWithSamplingPercentage:];
+[WAUtil customProcessInChargeOfDataProcessingForPolicies];
+[WAUtil isWildcardMacAddress:];
+[WAUtil getTokenForIdentifier:];
+[WAUtil logNestedDictionary:indent:prefix:];
+[WAUtil isWiFiFragmentSamplingEnabled];
+[WAUtil defaultKeysAllowedOnCustomerInstalls];
+[WAUtil getCopyOfMessage:withNumericalValuesSubstractedByValuesInMessage:];
+[WAUtil addFieldsForAuthFlagsLikeKey:inDict:];
+[WAUtil resourcePath];
+[WAUtil rotateUUIDsForMessage:];
+[WAUtil customMigrationOnProcess];
+[WAUtil getWeekStartForDate:];
+[WAUtil countTotalKeysIn:];
+[WAUtil isKeyBagUnlocked];
+[WAUtil canDeleteStore];
+[WAUtil sumNSNumberForKey:dstDict:otherDict:];
+[WAUtil isAnyWiFiAppInstalled];
+[WAUtil getMessageInstanceForKey:andGroupType:encodedSizeOut:];
+[WAUtil enableCoreDataConcurrencyDebug];
+[WAUtil customAgeOutTimeIntervalSecs];
+[WAUtil getNumberPreference:domain:];
+[WAUtil setFutureApfsPurgeableDeadline:forURL:];
+[WAUtil _getBaseTokenStorageKeychainQueryWithIdentifer:];
+[WAUtil deviceName];
+[WAUtil countTotalKeysInNSObject:];
+[WAUtil shouldProcessAnalyticsImmediately];
+[WAUtil customXPCStoreOnProcess];
```
