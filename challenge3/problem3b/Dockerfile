


# Use the official Ruby image as base
FROM ruby:2.3.1
# FROM debian:buster

# Set the working directory in the container
WORKDIR /app

# Install the specific version of Bundler required by your app
RUN gem install bundler -v '1.12.5'
# RUN apt-get update && apt-get install -y nodejs

# Copy the Gemfile and Gemfile.lock into the container
COPY ./github-languages/Gemfile /app/Gemfile
COPY ./github-languages/Gemfile.lock /app/Gemfile.lock

# Install dependencies
RUN bundle install

# FROM debian:buster

# # Install Node.js (JavaScript runtime)
# RUN apt-get update && apt-get install -y nodejs

# Copy the rest of the application code into the container
COPY ./github-languages /app

# Expose port 3000
EXPOSE 3000

# Start the Rails server
CMD ["rails", "server", "-b", "0.0.0.0"]
