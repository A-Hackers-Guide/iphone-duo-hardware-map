# `MLModelCollection`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 10 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSDictionary" _entries;
@"NSString" _deploymentID;
@"NSString" _namespaceName;
@"TRIClient" _trialClient;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_entries) entries;
@property (T@"NSString",C,N,V_deploymentID) deploymentID;
@property (T@"NSString",R,N,V_namespaceName) namespaceName;
@property (T@"TRIClient",R,N,V_trialClient) trialClient;
@property (T@"NSString",R,C,N,V_identifier) identifier;
```

## Class methods

```
+[MLModelCollection _namespaceNameFromCollectionIdentifier:];
+[MLModelCollection beginAccessingModelCollectionWithIdentifier:completionHandler:];
+[MLModelCollection endAccessingModelCollectionWithIdentifier:completionHandler:];
+[MLModelCollection getTrialClientClass];
+[MLModelCollection getTrialDownloadOptionsClass];
+[MLModelCollection getTrialExperimentIdentifiersClass];
+[MLModelCollection getTrialFactorClass];
+[MLModelCollection getTrialFactorLevelClass];
+[MLModelCollection getTrialFileClass];
+[MLModelCollection getTrialLevelClass];
```

## Instance methods

```
-[MLModelCollection entries];
-[MLModelCollection identifier];
-[MLModelCollection setEntries:];
-[MLModelCollection namespaceName];
-[MLModelCollection trialClient];
-[MLModelCollection initWithIdentifier:];
-[MLModelCollection deploymentID];
-[MLModelCollection _downloadOptions];
-[MLModelCollection _downloadWithProgress:];
-[MLModelCollection _endAccess];
-[MLModelCollection _handleTrialUpdateForNamespaceName:];
-[MLModelCollection _populateEntries];
-[MLModelCollection _register];
-[MLModelCollection _registerForUpdates];
-[MLModelCollection _setDeploymentID];
-[MLModelCollection setDeploymentID:];
```
