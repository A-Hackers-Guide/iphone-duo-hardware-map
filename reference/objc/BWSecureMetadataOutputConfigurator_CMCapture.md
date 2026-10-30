# `BWSecureMetadataOutputConfigurator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateLock;
@"BWSecureMetadataOutputConfiguration" _configurationForPrimaryClient;
@"NSMutableDictionary" _secondaryClientConfigurationsByClientID;
@"NSMutableDictionary" _maximumFrameRateByClientID;
@"NSMutableArray" _registeredAttachedSessionIDs;
@"BWSecureMetadataOutputConfiguration" _coalescedSecureMetadataOutputConfiguration;
@"<BWSecureMetadataOutputConfiguratorDelegate>" _delegate;
```

## Properties

```
@property (T@"BWSecureMetadataOutputConfiguration",&) configurationForPrimaryClient;
@property (T@"BWSecureMetadataOutputConfiguration",R) coalescedSecureMetadataOutputConfiguration;
@property (T@"<BWSecureMetadataOutputConfiguratorDelegate>",N) delegate;
```

## Class methods

```
+[BWSecureMetadataOutputConfigurator initialize];
```

## Instance methods

```
-[BWSecureMetadataOutputConfigurator init];
-[BWSecureMetadataOutputConfigurator dealloc];
-[BWSecureMetadataOutputConfigurator setDelegate:];
-[BWSecureMetadataOutputConfigurator delegate];
-[BWSecureMetadataOutputConfigurator _coalescedClientConfiguration];
-[BWSecureMetadataOutputConfigurator _updateSecureMetadataOutputConfigurationForceDelegate:];
-[BWSecureMetadataOutputConfigurator coalescedSecureMetadataOutputConfiguration];
-[BWSecureMetadataOutputConfigurator configurationForPrimaryClient];
-[BWSecureMetadataOutputConfigurator registerAttachedSessionID:];
-[BWSecureMetadataOutputConfigurator resetAllConfigurations];
-[BWSecureMetadataOutputConfigurator setConfiguration:forAttachedSessionID:];
-[BWSecureMetadataOutputConfigurator setConfigurationForPrimaryClient:];
-[BWSecureMetadataOutputConfigurator setMaximumFrameRate:forAttachedSessionID:];
-[BWSecureMetadataOutputConfigurator unregisterAttachedSessionID:];
```
