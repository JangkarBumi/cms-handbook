# Fatgoat Handbook | All Remote Startup Accelerator

# About Us

## A Different Breed of Startup Incubator

We incubate, accelerate, and implement ideas that our team create internally.

## Work From Home

We're a 100% remote company. Work from anywhere in the world.

## Radical Transparency

We believe in radical transparency, where the best ideas win. As such, how we run the company is [open sourced to the world](https://github.com/avancevl/avancevl.github.io). In this central repository, you will find all the information you need to understand what it is like to work here. All the information available to our employees is also available to you. We encourage you to learn more about us here at this depository.

## Work with the best people

We want to work with talented individuals and are **always actively hiring**.

[Explore opportunities](https://avancevl.github.io/recruit/recruit.html)

## Open Feedback

We welcome feedback.

- Please make a [pull request](https://github.com/avancevl/avancevl.github.io/pull/new/master) to suggest improvements or add clarification.
- Please create a [issue](https://github.com/avancevl/avancevl.github.io/issues/new) to ask questions.

## Community

Help us support the open source, startup, developer communites in Taiwan by following:

- [Startup Jobs Taiwan :rocket:](https://021tw.github.io/)
- [Full Stack Developers Taiwan :star:](https://stacktw.github.io/)

<br>

# How To Build

## Environment build on Mac

1. Install Homebrew

   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
   ```

1. Install the latest version of Python3.

   ```
   brew install python
   ```

1. Install `pip`.
   1. `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
   1. `python3 get-pip.py`
1. Install Python packages.
   1. `pip install beautifulsoup4`
   1. `pip install python-frontmatter`

## Environment build on Windows

1. Pythone website download and install the latest version of Python3. <https://www.python.org/downloads/>

2. Installing `pip`

   ```
   python get-pip.py
   ```

3. Install Python packages.
   1. `pip install beautifulsoup4`
   2. `pip install python-frontmatter`

## Edit markdown and build

1. Edit markdown files in `_main` folder, **DO NOT** edit files in `_page` folder.
1. Run `python3 i18n.py` to generate language specific markdown files in `_page` folder.
1. Commit and push to deploy to [avancevl.github.io](https://avancevl.github.io)

# How to add new language

## Configuration

Locales are configured in `_config.yml` adding Malaysian (my):

    locales:
        en:
            baseurl: "/en"
            name: English
            lang: en
        zh-tw:
            baseurl: "/zh-tw"
            name: 繁體
            lang: zh-tw
        zh-cn:
            baseurl: /zh-cn
            name: 简体
            lang: zh-cn
        my:
            baseurl: /my
            name: Malaysian
            lang: my

## Content

Edit markdown files use language tag `<a name="my"></a>` after Malaysian(my) content in \_main folder, and you can set the predefined variables at the beginning of the archive between triple-dashed lines(see below for a reference).

    ---
    layout: default
    title: Sari Handbook
    description: For All Remote Teams
    locales:
        zh-tw:
            title: Sari手冊
            description: 全遠端工作團隊
        zh-cn:
            title: Sari手册
            description: 全远端工作团队
        en:
            title: Sari Handbook
            description: For All Remote Teams
        my:
            title: Buku Panduan Sari
            description: Untuk Semua Pasukan Jauh
    ---

## Navigation

Edit translation menu file `navigation.yml` in \_data folder, if there is no setting, use the default language.

    - page:
        zh-tw: ":couple: 團隊"
        zh-cn: ":couple: 团队"
        en: ":couple: Team"
        my: ":couple: pasukan"
    url: /team

## Language

Set layout language file `language.yml` in \_data folder, if there is no setting, use the default language.

    my:
        VIEW_JOB_OPENINGS: View Jobs
        SELECT_LANGUAGE: Language
        ALL_REMOTE_STARTUP_IN: All Remote Startup Incubator
        FOLLOW_US: Follow Us
        CONTACT_US: Contact Us
        TITLE_SARI: Sari Handbook

```bash
#Install rbenv

brew install rbenv
```

```bash
#Install ruby version

rbenv install 3.0.0
```

```bash
#Add PATH

export PATH="$HOME/.rbenv/bin:$PATH"
export PATH=/usr/local/lib/ruby/gems/2.7.1/bin:$PATH
eval "$(rbenv init -)"
```

```bash
#How to install

bundle install
```

```bash
#Install Jekyll

gem install bundler jekyll
```

```bash
#If ruby >3.0.0

bundle add webrick
```

```bash
#How to run

bundle exec jekyll serve
```

```bash
#How to add new landing pages

1. Create new markdown file your-page-name.md in the root
2. Use default layout and change the title to your-page-name
```
