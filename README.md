[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com) [![Build Status](https://travis-ci.org/9cookies/serverless-aws-documentation.svg?branch=master)](https://travis-ci.org/9cookies/serverless-aws-documentation) [![codecov](https://codecov.io/gh/9cookies/serverless-aws-documentation/branch/master/graph/badge.svg)](https://codecov.io/gh/9cookies/serverless-aws-documentation)

[![LinkedIn][linkedin-shield]][linkedin-url]

<h3 align="center">Serverless Project</h3>

  <p align="center">
    <a href="https://careertutor.fractalslab.com/">View Demo</a>
  </p>




<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
        <a href="#why-different">Why this repo is different than other typical github repos</a>
    </li>
    <li>
        <a href="">AWS system block diagram</a>
        </li>
    <li>
<a href="">Configuration</a>
</li>
    <li>
<a href="">Continuous integration (CI)</a>
</li>
    <li>
<a href="">Deployment</a>
</li>
    <li>
<a href="">Contact us</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->


### Why this repository different from other difficult repository?

We are using:

* [Python PEP8 standard (black, isort, flake8)](https://github.com/saifulazad/career-tutor/blob/master/.pre-commit-config.yaml)
* [Unit test coverage](https://github.com/saifulazad/career-tutor/tree/master/tests)
* [CI integration by github-action](https://github.com/saifulazad/career-tutor/blob/master/.github/workflows/python-app.yml)


## AWS system block diagram

[![Product Name Screen Shot][product-screenshot]](https://careertutor.fractalslab.com/)

## Configuration
- create a `config.py` folder under `cvService` folder
- Paste the content in `config.py`
    ~~~
    RECAPTCHA_SECRET = '6LeBJ30dAAAAANm4aX9wRTzSnbk-9d7iBMsJkwi9'
    FIXED_RECAPTCHA_SECRET = '82a83229-1b77-4567-89be-72e137676de7'
    ~~~

## Getting Started

This is a simple serverless project using AWS services. First create a s3 bucket for deploying our static content like
html, css and js files. Create cloud font for redirect website url http to https. We need two API endpoints for POST our
data.

#### Host a Static Website

Static websites deliver HTML, JavaScript, images, video and other files for need a website visitors. Static websites are
very low cost, provide high-levels of reliability, require almost no IT administration, and scale to handle
enterprise-level traffic with no additional work.

[Configuring a static website on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html)

### How it works?

Route 53 sends automated requests over the internet to a resource, such as a web server, to verify that it's reachable,
available, and functional.

### Install

#### via NPM

Install the serverless CLI via NPM:

```shell
  npm install -g serverless
```

#### Initial setup

Run the command below and follow the prompts:

```shell
  serverless
```

#### Setup with the aws-cli

To set them up through the _aws-cli_ install it first then run aws configure to configure the aws-cli and credentials:

```shell
  aws configure
```

Credentials are stored in INI format in ~_/.aws/credentials_, which you can edit directly if needed.

### GitHub Build

GitHub-hosted runners have a tools cache with pre-installed software, which includes Python and PyPy. For more
information, see
[GitHub Actions](https://docs.github.com/en/actions/learn-github-actions)

### Deploy

#### Deployment without stage and region options

```shell
  serverless deploy
```

This is the simplest deployment usage possible. With this command Serverless will deploy your service to the defined
provider in the default stage (dev).

#### Deployment with stage and region options

```shell
    serverless deploy --stage=prod --region=ap-southeast-1
```

With this example we've defined that we want our service to be deployed to the production stage in the region
ap-southeast-1.




<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

<!-- CONTACT -->

## Contact

Saiful Azad - [mr.saiful.azad@gmail.com](mr.saiful.azad@gmail.com)


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://www.linkedin.com/in/saifulazad/

[product-screenshot]: images/screenshot.jpg
