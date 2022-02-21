Name:          mybatis-generator
Version:       1.3.2
Release:       2
Summary:       A code generator for MyBatis and iBATIS
License:       ASL 2.0
URL:           http://www.mybatis.org/
Source0:       https://github.com/mybatis/generator/archive/%{name}-%{version}.tar.gz
BuildRequires: mvn(log4j:log4j:1.2.17) mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-launcher) mvn(junit:junit)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.mybatis:mybatis) mvn(org.hsqldb:hsqldb)
BuildRequires: mvn(org.mybatis:mybatis-parent:pom:)
BuildRequires: mvn(org.apache.commons:commons-ognl)
BuildRequires: maven-local maven-enforcer-plugin maven-plugin-bundle
BuildRequires: maven-plugin-plugin maven-surefire-report-plugin
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildArch:     noarch

%description
MyBatis Generator (MBG) is a code generator for MyBatis and iBATIS.

%package maven-plugin
Summary:       MyBatis Generator Maven Plugin

%description maven-plugin
MyBatis Generator Maven Plugin.

%package systests-common
Summary:       MyBatis Generator Tests (Common Classes)

%description systests-common
MyBatis Generator Tests (Common Classes).

%package systests-mybatis3
Summary:       MyBatis Generator Tests (MyBatis3)

%description systests-mybatis3
MyBatis Generator Tests (MyBatis3).

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n generator-%{name}-%{version}

%pom_remove_dep :cobertura
%pom_remove_dep :cobertura mybatis-generator-systests-mybatis3
%pom_xpath_remove "pom:dependency[pom:artifactId= '%{name}-core']/pom:classifier" %{name}-systests-mybatis3

%pom_remove_dep :cobertura mybatis-generator-systests-ibatis2-java2
%pom_xpath_remove "pom:dependency[pom:artifactId= '%{name}-core']/pom:classifier" %{name}-systests-ibatis2-java2
%pom_remove_dep :cobertura mybatis-generator-systests-ibatis2-java5
%pom_xpath_remove "pom:dependency[pom:artifactId= '%{name}-core']/pom:classifier" %{name}-systests-ibatis2-java5

%pom_disable_module %{name}-systests-ibatis2-java2
%pom_disable_module %{name}-systests-ibatis2-java5
%pom_remove_dep :ibatis-sqlmap

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-gcu-plugin %{name}-core
%pom_remove_plugin :jdepend-maven-plugin %{name}-core
%pom_remove_plugin :maven-install-plugin %{name}-core
%pom_remove_plugin :maven-assembly-plugin %{name}-core
%pom_remove_plugin :maven-javadoc-plugin %{name}-core
%pom_remove_plugin :maven-release-plugin %{name}-core
%pom_remove_plugin :maven-site-plugin %{name}-core
%pom_remove_plugin :maven-source-plugin %{name}-core
%pom_remove_plugin :cobertura-maven-plugin %{name}-core
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" %{name}-core

%pom_add_dep org.apache.commons:commons-ognl::test mybatis-generator-systests-mybatis3

sed -i 's/\r//' LICENSE NOTICE %{name}-core/doc/*

%mvn_package ":%{name}" %{name}
%mvn_package ":%{name}-core" %{name}

%build

%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-%{name}
%doc %{name}-core/doc/*
%license LICENSE NOTICE

%files maven-plugin -f .mfiles-%{name}-maven-plugin
%license LICENSE NOTICE

%files systests-common -f .mfiles-%{name}-systests-common
%license LICENSE NOTICE

%files systests-mybatis3 -f .mfiles-%{name}-systests-mybatis3
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Mon Feb 21 2022 wangkai <wangkai385@huawei.com> - 1.3.2-2
- Rebuild for fix log4j1.x cves

* Mon May 10 2021 chengzihan <chengzihan2@huawei.com> - 1.3.2-1
- Package init
